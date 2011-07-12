"""
Interface to a model program (python module) used by ProductModelProgram 
"""

# Actions a are still function objects (not aname strings) here
# because composition happens in ProductModelProgram, a level above.

import sys
import copy
import inspect
import itertools

class ModelProgram(object):

  def __init__(self, module, exclude, include):
    self.module = module
    self.exclude = exclude
    self.include = include

    # recognize PEP-8 style names (all lowercase) if present
    if hasattr(self.module, 'accepting'):
      self.module.Accepting = self.module.accepting
    if hasattr(self.module, 'statefilter'):
      self.module.StateFilter = self.module.statefilter
    if hasattr(self.module, 'state_filter'):
      self.module.StateFilter = self.module.state_filter
    if hasattr(self.module, 'reset'):
      self.module.Reset = self.module.reset

    # assign defaults to optional attributes
    if not hasattr(self.module, 'enablers'):
      self.module.enablers = dict() # all actions always enabled
    if not hasattr(self.module, 'cleanup'):
      self.module.cleanup = tuple() # no cleanup actions
    if not hasattr(self.module, 'domains'):
      self.module.domains = dict() # empty domains
    if not hasattr(self.module, 'combinations'):
      self.module.combinations = dict() # 'all', Cartesian product
    if not hasattr(self.module, 'Accepting'):
      self.module.Accepting = self.TrueDefault
    if not hasattr(self.module, 'StateFilter'):
      self.module.StateFilter = self.TrueDefault
    if not hasattr(self.module, 'observables'):
      self.module.observables = tuple() # no observable actions

  def make_argslist(self, a):
    """
    Parameter generator: return list of all args combos for action symbol a
    """
    arginfo = inspect.getargspec(a)# ArgInfo(args,varargs,keywords,locals)
    if arginfo[0]:
      args = arginfo[0] # usual case: fixed sequence of positional arguments
    elif arginfo[1]:
      args = [arginfo[1]] # special case: either no arg, or one exception arg
    else:
      args = () # no arguments anywhere, args must have this value
    domains = [ self.module.domains[a][arg]() # evaluate state-dependent domain
                if callable(self.module.domains[a][arg]) 
                else self.module.domains[a][arg] # look up static domain
                for arg in args if a in self.module.domains ]
    combination = self.module.combinations.get(a, 'all')  # default is 'all'
    if combination == 'cases': # as many args as items in smallest domain
      argslists = zip(*domains)
    elif combination == 'all':   # Cartesian product
      argslists = itertools.product(*domains)
    # might be nice to support 'pairwise' also
    # return tuple not list, hashable so it can be key in dictionary 
    # also handle special case (None,) indicates empty argslist in domains
    return tuple([() if x == (None,) else x for x in argslists ]) 

  def MakeActions(self):
    # separate function from __init__, call after all modules imported
    # need copy, might not be same as self.module.actions due to include/excl
    # note self.actions can include shared but unused actions
    self.actions = list(self.module.actions)
    if self.exclude:
      self.actions = [ a for a in self.actions if a.__name__ not in self.exclude ]
    if self.include:
      self.actions = [ a for a in self.actions if a.__name__ in self.include ]
    self.cleanup = list(self.module.cleanup) # need a copy, may change it below
    if self.exclude:
      self.cleanup = [ c for c in self.cleanup if c.__name__ not in self.exclude ]
    if self.include:
      self.cleanup = [ c for c in self.cleanup if c.__name__ in self.include ]

  def ParamGen(self):
    #print 'ModelProgram ParamGen for', self.module.__name__ #DEBUG
    #print '  actions ', self.actions
    #print '  domains ', self.module.domains
    self.argslists = dict([(a, self.make_argslist(a))
                           for a in self.actions
                           if not a in self.module.observables ])
    
  def TrueDefault(self):
    return True

  def Properties(self):
    return  { 'accepting': self.module.Accepting(),
              'statefilter': self.module.StateFilter() }

  def Reset(self):
    try:
      self.module.Reset()
    except AttributeError: # Reset is optional, but there is no default
      print 'No Reset function for model program %s' % self.module.__name__
      sys.exit()       

  def ActionEnabled(self, a, args):
    """
    action a with args is enabled in the current state
    """
    return (a not in self.module.enablers 
            or self.module.enablers[a][0](*args))
            # Assumes enablers[a] has only one item, always true in this version

  def Transitions(self, actions, argslists): 
    """
    Return tuple for all enabled transitions:
     (action, args, result, next state, properties)
    Pass appropriate params for observable or controllable actions + argslists
    """
    enabled = list()
    for a in actions:
      enabled += [(a, args) + self.GetNext(a,args) # (a,args,result,next,prop's)
                  for args in argslists[a] if self.ActionEnabled(a, args) ]
    return [(a,args,result,next,properties)
            for (a,args,result,next,properties) in enabled 
            if properties['statefilter']]
  
  def EnabledTransitions(self, argslists, cleanup=False):
    """
    Return tuple for all enabled observable and controllable transitions:
     (action, args, result, next state, properties)
    """
    actions = self.cleanup if cleanup else self.actions
    controllableActions = set(actions) - set(self.module.observables)
    observableActions = set(argslists.keys()) & set(self.module.observables)
    if cleanup:
      observableActions = set(observableActions) & set(self.cleanup)
    enabled = list()
    # Controllable actions use self.argslists assigned by ParamGen
    enabled += self.Transitions(controllableActions, self.argslists)
    # Observable actions use argslists parameter here
    enabled += self.Transitions(observableActions, argslists)
    return enabled

  def DoAction(self, a, args):
    """
    Execute action in model, update state,
    """
    return a(*args)

  def Current(self):
    """
    Return current state, a dictionary of variable names to values
    This is used to save/restore states, so make deep copies of values
    """
    return dict([(vname, copy.deepcopy(getattr(self.module, vname)))
                  for vname in self.module.state ])

  def Restore(self, state):
    """
    Restore state
    """
    self.module.__dict__.update(state)
     
  def GetNext(self, a, args):
    """
    Return result and next state, given action and args. 
    Nondestructive, restores state.
    also return dict. of properties of next state as third element in tuple
    """
    saved = self.Current()    
    result = self.DoAction(a, args)
    next = self.Current()
    properties = self.Properties() # accepting state, etc.
    self.Restore(saved)
    return (result, next, properties)
