"""
Interface to an FSM module (graph) used by ProductModelProgram
"""

class FSM(object):
 
  def __init__(self, module):
    self.module = module
    self.current = self.module.initial # raise exception if module is not FSM
    if not hasattr(self.module, 'actions'):
      self.actions = self.actions_in_graph() # default
    else:
      self.actions = self.module.actions # not a copy, no include/exclude
    if not hasattr(self.module, 'cleanup'):
      self.module.cleanup = tuple() # else just use the ones already there

  def actions_in_graph(self):
    return tuple(set([ action for (current, (action,args,result), next) in 
                       self.module.graph]))

  def make_properties(self, state):
    return { 'accepting': state in self.module.accepting, 'statefilter': True }

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
                for (current,(action,args,result),next) in self.module.graph 
                if action in self.module.cleanup] 
    else:
      graph = self.module.graph
    return graph

  def ActionEnabled(self, a, args):
    """
    action a with args is enabled in the current state
    """
    graph = CleanupGraph(cleanup)
    return any([(a == action and args == arguments)
                for (current,(action, arguments, result),next) in graph
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
             for (current,(action,args,result),next) in self.module.graph 
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
