"""
Interface to a test suite module (one or more runs) used by ProductModelProgram
"""

from operator import concat

class TestSuite(object):

  def __init__(self, module, exclude, include):
    self.module = module
    self.exclude = exclude
    self.include = include

    # recognize PEP-8 style names (all lowercase) if present
    if hasattr(self.module, 'testsuite'):
      self.module.testSuite = self.module.testsuite
    if hasattr(self.module, 'test_suite'):
      self.module.testSuite = self.module.test_suite

    # assign defaults to optional attributes
    if not hasattr(self.module, 'observables'):
      self.module.observables = tuple() # no observable actions

    self.irun = 0 # index of current test run in test suite
    self.pc = 0 # program counter
    if hasattr(self.module, 'actions'):
      self.actions = list(self.module.actions) # copy, actions from cmd line
    else:
      self.actions = list(self.actions_in_suite()) # default, copy
    # Account for exclude, actions options, copy code in ModelProgram.
    # Can't easily factor this out to caller ProductModelProgram because
    # self.actions list is constructed differently in each type of model
    # elsewhere in this module it says we can ignore cleanup, but ...
    if self.exclude:
      self.actions = [ a for a in self.actions if a.__name__ not in self.exclude ]
    if self.include:
      self.actions = [ a for a in self.actions if a.__name__ in self.include ]
    # Is cleanup even meaningful for test suite?
    if not hasattr(self.module, 'cleanup'):
      self.cleanup = tuple() # else just use the ones already there
    else:
      self.cleanup = list(self.module.cleanup) # need a copy, may change it below
    if self.exclude:
      self.cleanup = [ c for c in self.cleanup if c.__name__ not in self.exclude ]
    if self.include:
      self.cleanup = [ c for c in self.cleanup if c.__name__ in self.include ]
    # Revise the test suite to account for excluded, included actions
    self.test_suite = list()
    for run in self.module.testSuite:
       new_run = list() # list not tuple, must mutable
       for action in run:
         if action[0] in self.actions:
           new_run.append(action)
         else:
           break # truncate the run before the excluded action
       self.test_suite.append(new_run)
    # replace self.module.testSuite with self.test_suite below

  def actions_in_suite(self):
    # there might be two or three items in action_tuple
    return tuple(set(reduce(concat,[[action_tuple[0] for action_tuple in run]
                                    for run in self.module.testSuite])))

  def Accepting(self):
    # In a test suite, the only accepting states are at ends of runs
    # NB Here Accepting() is called *after* DoAction() that advances self.pc
    length = len(self.test_suite[self.irun]) # number of tuples in run
    return (self.pc == length)

  def make_properties(self, accepting):
    return  { 'accepting': accepting, 'statefilter': True,
              'stateinvariant': True }

  def Properties(self):
    return self.make_properties(self.Accepting())

  def Reset(self): # needed by stepper
    self.pc = 0
    if self.irun < len(self.test_suite) - 1:
      self.irun += 1
    else:
      raise StopIteration # no more runs in test suite     

  def ActionEnabled(self, a, args):
    """
    action a with args is enabled in the current state
    """
    step = self.test_suite[self.irun][self.pc]
    action, arguments = step[0:2] # works whether or not step has result
    return (a == action and args == arguments)

  def EnabledTransitions(self, cleanup=False):
    """
    Return list of all tuples for enabled actions.  Here, there is just one.
    (action, args, next state, next state is accepting state)
    Next state is a list of two elements:the run number and step within the run
    In a test suite, there is always just *one* next action, or *none*
    Ignore cleanup, test suite should always end in accepting state.
    """
    run = self.test_suite[self.irun]
    length = len(run)
    if self.pc < length:
      step = run[self.pc]
      action, args = step[0:2]
      result = step[2] if len(step) > 2 else None # result is optional
      next = self.pc + 1
      accepting = (next == length)
      return([(action, args, result, (self.irun,next),
               self.make_properties(accepting))])
    else:
      return list() # test run finished, nothing enabled, 

  def DoAction(self, a, args):
    step = self.test_suite[self.irun][self.pc]
    result = step[2] if len(step) > 2 else None # result is optional
    self.pc += 1
    return result

  def Current(self):
    return (self.irun, self.pc) 

  def Restore(self, state):
    """
    Restore state
    """
    self.irun, self.pc = state
     
  # GetNext not needed
