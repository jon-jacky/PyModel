"""
Interface to an FSM module (graph) used by ProductModelProgram
"""

from model import Model

class FSM(Model):

  def __init__(self, module, exclude, include):
    Model.__init__(self, module, exclude, include)

  def post_init(self):
    """
    Now that all modules have been imported and executed their __init__
     do a postprocessing pass
     to process metadata that might be affected by configuration modules
    """
    # Do all of this work here rather than in __init__
    #  so it can include the effects of any pymodel config modules

    # Make copies of collections that may be altered later
    # self.actions is not used in this module outside this __init__
    #  BUT it is used in several places in Model and ProductModelProgram
    # EnabledTransitions below works directly on self.module.graph,
    #  not self.actions
    if not hasattr(self.module, 'actions'):
      self.actions = list(self.actions_in_graph()) # default, make copy
    else:
      self.actions = list(self.module.actions) # copy
    Model.post_init(self) # uses self.actions
    # Construct self.graph like self.module.graph 
    #  BUT also accounts for include, exclude via self.actions
    self.graph = [ (current, (action,args,result), next) 
                   for (current, (action,args,result), next) in
                   self.module.graph if action in self.actions ]
    # prepare for first run
    self.current = self.module.initial # raise exception if module is not FSM


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
