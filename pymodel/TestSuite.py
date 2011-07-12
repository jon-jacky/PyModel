"""
Interface to a test suite module (one or more runs) used by ProductModelProgram
"""

from operator import concat

class TestSuite(object):

  def __init__(self, module):
    self.module = module

    # recognize PEP-8 style names (all lowercase) if present
    if hasattr(self.module, 'testsuite'):
      self.module.testSuite = self.module.testsuite
    if hasattr(self.module, 'test_suite'):
      self.module.testSuite = self.module.test_suite

    self.testSuite = self.module.testSuite # exception if module not TestSuite
    self.irun = 0 # index of current test run in test suite
    self.pc = 0 # program counter
    if hasattr(self.module, 'actions'):
      self.actions = self.module.actions # not a copy, no include/exclude
    else:
      self.actions = self.actions_in_suite() # default

  def actions_in_suite(self):
    # there might be two or three items in action_tuple
    return tuple(set(reduce(concat,[[action_tuple[0] for action_tuple in run]
                                    for run in self.module.testSuite])))

  def Accepting(self):
    # In a test suite, the only accepting states are at ends of runs
    # NB Here Accepting() is called *after* DoAction() that advances self.pc
    length = len(self.module.testSuite[self.irun]) # number of tuples in run
    return (self.pc == length)

  def make_properties(self, accepting):
    return  { 'accepting': accepting, 'statefilter': True }

  def Properties(self):
    return self.make_properties(self.Accepting())

  def Reset(self): # needed by stepper
    self.pc = 0
    if self.irun < len(self.module.testSuite) - 1:
      self.irun += 1
    else:
      raise StopIteration # no more runs in test suite     

  def ActionEnabled(self, a, args):
    """
    action a with args is enabled in the current state
    """
    step = self.module.testSuite[self.irun][self.pc]
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
    run = self.module.testSuite[self.irun]
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
    step = self.module.testSuite[self.irun][self.pc]
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
