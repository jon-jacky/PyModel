"""
Analyzer functions
"""

import sys
import os.path
from copy import deepcopy

# rebind in explore

anames = list()

states = list() # state's index here is its state number in lists, graph below

initial = 0 # always, keep as well as runstarts (below) for backward compat.

accepting = list()
frontier = list() # unexplored states in graph, may add more transitions
finished = list() # terminal states that are accepting states
deadend = list() # terminal states that are not accepting states
runstarts = list() # initial states of test runs after the first, if any

graph = list() # a set (no dups) but we want a sequence to see them in order

def explore(mp, maxTransitions):
    # some globals may not be needed; code only mutates collection *contents*, 
    # as in finished, deadend
    global anames, states, graph, accepting, frontier
    anames = mp.anames
    explored = list() 
    fsm = list() # list of transitions with mp states not state numbers
    more_runs = True # TestSuite might have multiple runs
    while more_runs:
      initialState = mp.Current()
      frontier.append(initialState)
      states.append(initialState) # includes initial state even if no trans'ns
      iInitial = states.index(initialState) # might already be there
      runstarts.append(iInitial)
      if mp.Accepting(): # initial state might be accepting even if no trans'ns
        accepting.append(iInitial)
      while frontier:
        if len(graph) == maxTransitions:
            break
        current = frontier[0]   # head, keep in mind current might lead nowhere
        frontier = frontier[1:] # tail
        icurrent = states.index(current) # might already be there
        #print 'current %s' % current # DEBUG
        #print '   frontier %s' % frontier # DEBUG
        explored.append(current) # states we checked, some might lead nowhere
        mp.Restore(deepcopy(current)) # assign state in mp, need deepcopy here
        transitions = mp.EnabledTransitions(list()) # all actions, not cleanup
        if not transitions: # terminal state, no enabled transitions
          if icurrent in accepting:
            finished.append(icurrent)
          else:
            deadend.append(icurrent)
        # print 'current %s, transitions %s' % (current, transitions) # DEBUG
        for (aname, args, result, next, next_properties) in transitions:
          # EnabledTransitions doesn't return transitions where not statefilter
          # if next_properties['statefilter']: 
            if len(graph) < maxTransitions:
                if next not in explored and next not in frontier:
                    # append for breadth-first, push on head for depth-first
                    frontier.append(next) # frontier contents are already copies
                transition = (current, (aname, args, result), next)
                if transition not in fsm:
                    fsm.append(transition)
                    if current not in states:
                        states.append(current)
                    if next not in states:
                        states.append(next) # next might never be in explored
                    # icurrent = states.index(current) # might already be there
                    inext = states.index(next) # ditto
                    graph.append((icurrent, (aname,args,result), inext)) #tuple
                    if mp.Accepting() and icurrent not in accepting:
                        accepting.append(icurrent)
                    if next_properties['accepting'] and inext not in accepting:
                        accepting.append(inext)
                    # TK likewise unsafe states, dead states
            else: # found transition that will not be included in graph
                frontier.insert(0,current) # not completely explored after all
                # explored.remove(current) # not necessary
                break
            # end if < ntransitions else ...
        # end for transitions
      # end while frontier
     
      # continue exploring test suite with multiple runs
      more_runs = False
      if mp.TestSuite:
          try:
              mp.Reset()
              more_runs = True
          except StopIteration: # raised by TestSuite Reset after last run
              pass # no more runs, we're done
    # end while more_runs
        

def actiondef(aname):
    return 'def %s(): pass' % aname

def state(i, state):
    return '%s : %s,' % (i, state)


def initial_state(): # all FSMs
    return 'initial = %s' % initial

def runstarts_states(): # initial states of test runs after the first, if any
    return 'runstarts = %s' % runstarts

def accepting_states():
    return 'accepting = %s' % accepting

def frontier_states():
    return 'frontier = %s' % [ states.index(s) for s in frontier ]

def finished_states():
    return 'finished = %s' % finished

def deadend_states():
    return 'deadend = %s' % deadend

def quote_string(x): # also appears in Dot
    if isinstance(x,tuple):
        return str(x)
    else:
        return "'%s'" % x if isinstance(x, str) else "%s" % x

def transition(t):
    # return '%s' % (t,) # simple but returns quotes around action name
    current, (action, args, result), next = t
    return '(%s, (%s, %s, %s), %s)' % (current, action, args, 
                                       quote_string(result), next)

def save(name):
    f = open("%s.py" % name, 'w')
    f.write('\n# %s' % os.path.basename(sys.argv[0])) # echo command line ...
    f.write(' %s\n' % ' '.join(['%s' % arg for arg in sys.argv[1:]])) # ...etc.
    f.write('# %s states, %s transitions, %s accepting states, %s finished and %s deadend states\n' % \
            (len(states),len(graph),len(accepting),len(finished),len(deadend)))
    f.write('\n# actions here are just labels, but must be symbols with __name__ attribute\n\n')
    f.writelines([ actiondef(aname)+'\n' for aname in anames ])
    f.write('\n# states, key of each state here is its number in graph etc. below\n\n')
    f.write('states = {\n')
    for i,s in enumerate(states):
        f.write('  %s\n' % state(i,s))
    f.write('}\n')
    f.write('\n# initial state, accepting states, frontier states, deadend states\n\n')
    f.write('%s\n' % initial_state())
    f.write('%s\n' % accepting_states())
    f.write('%s\n' % frontier_states())
    f.write('%s\n' % finished_states())
    f.write('%s\n' % deadend_states())
    f.write('%s\n' % runstarts_states())
    f.write('\n# finite state machine, list of tuples: (current, (action, args, result), next)\n\n')
    f.write('graph = (\n')
    f.writelines([ '  %s,\n' % transition(t) for t in graph ])
    f.write(')\n')
    f.close()
