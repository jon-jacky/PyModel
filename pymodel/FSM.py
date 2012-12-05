"""
Interface to an FSM module (graph) used by ProductModelProgram
"""

class FSM(object):
 
  def __init__(self, module, exclude, include):
    self.module = module
    self.exclude = exclude
    self.include = include
    self.current = self.module.initial # raise exception if module is not FSM
    # Assign defaults to optional attributes
    # need copy, might not be same as self.module.actions due to include/excl
    # This FSM self.actions is not used in this module outside this __init__
    #  BUT it is used in several places in ProductModelProgram
    # EnabledTransitions below works directly on self.module.graph,
    #  not self.actions
    if not hasattr(self.module, 'actions'):
      self.actions = list(self.actions_in_graph()) # default, make copy
    else:
      self.actions = list(self.module.actions) # copy
    if not hasattr(self.module, 'cleanup'):
      self.module.cleanup = tuple() # else just use the ones already there
    if not hasattr(self.module, 'observables'):
      self.module.observables = tuple() # no observable actions
    # Account for exclude, actions options, copy code in ModelProgram.
    # Can't easily factor this out to caller ProductModelProgram because
    # self.actions list is constructed differently in each type of model
    if self.exclude:
      self.actions = [ a for a in self.actions if a.__name__ not in self.exclude ]
    if self.include:
      self.actions = [ a for a in self.actions if a.__name__ in self.include ]
    self.cleanup = list(self.module.cleanup) # need a copy, may change it below
    if self.exclude:
      self.cleanup = [ c for c in self.cleanup if c.__name__ not in self.exclude ]
    if self.include:
      self.cleanup = [ c for c in self.cleanup if c.__name__ in self.include ]
    # Construct self.graph like self.module.graph 
    #  BUT also accounts for include, exclude via self.actions
    self.graph = [ (current, (action,args,result), next) 
                   for (current, (action,args,result), next) in
                   self.module.graph if action in self.actions ]

  def actions_in_graph(self):
    return tuple(set([ action for (current, (action,args,result), next) in 
                       self.module.graph])) # not self.graph, here ONLY

  def make_properties(self, state):
    return { 'accepting': state in self.module.accepting, 'statefilter': True,
             'stateinvariant': True }

  def Properties(self):
    return self.make_properties(self.current)
  
  def Reset(self): # needed by stepper
    self.current = self.module.initial

  def CleanupGraph(self, cleanup=False):
    """
    if cleanup, return the graph with just the cleanup transitions
    """
    if cleanup:
      graph = [(current,(action,args,result),next)
                for (current,(action,args,result),next) in self.graph 
                if action in self.module.cleanup] 
    else:
      graph = self.graph
    return graph

  def ActionEnabled(self, a, args):
    """
    action a with args is enabled in the current state
    """
    # no cleanup check here
    # any args matches empty arguments in FSM
    return any([(a == action and (not arguments or args == arguments))
                for (current,(action, arguments, result),next) 
                in self.graph
                if current == self.current ])

  def EnabledTransitions(self, cleanup=False):
    """
    Return list tuples for all enabled actions: 
    (action, args, next state, properties)
    """
    graph = self.CleanupGraph(cleanup)
    return [(action, args, result, next, self.make_properties(next))
            for (current,(action,args,result),next) in graph 
            if current == self.current ]

  def DoAction(self, a, arguments):
    ts = [(current,(action,args,result),next)
             for (current,(action,args,result),next) in self.graph 
             if current == self.current and action == a 
             and args == arguments[0:len(args)]] #ignore extra trailing args
    # print 'List ts %s' % ts # DEBUG
    # Might be nondet. FSM: for now, just pick first transition that matches
    current, (action,args,result), self.current = ts[0] 
    return result

  def Current(self):
    return self.current

  def Restore(self, state):
    self.current = state

  # GetNext not needed
