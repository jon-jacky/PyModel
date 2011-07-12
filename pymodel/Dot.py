"""
Dot - generate graphics in dot language
"""

import os.path

def node(n, fsm):
    try: # FSM modules written by PyModel Analyzer have frontier attribute etc.
        frontier = fsm.frontier
        finished = fsm.finished
        deadend = fsm.deadend
        runstarts = fsm.runstarts
    except AttributeError: # FSM modules written by hand may not have these
        frontier = list()
        finished = list()
        deadend = list()
        runstarts = list()
    return '%s [ style=filled, shape=ellipse, peripheries=%s, fillcolor=%s' % \
        (n, 2 if n in fsm.accepting else 1, # peripheries
         'orange' if n in frontier else # high priority, analysis inconclusive
         'yellow' if n in deadend else
         'lightgreen' if n in finished else
         'lightgray' if n == fsm.initial or n in runstarts else #lowest priority
         'white') # other states

def state(n, fsm, noStateTooltip):
    if noStateTooltip:
        return '%s ]' % node(n,fsm)
    else:
        return '%s,\n      tooltip="%s" ]' % (node(n,fsm), fsm.states[n])


def quote_string(x): # also appears in Analyzer
    if isinstance(x,tuple):
        return str(x)
    else:
        return "'%s'" % x if isinstance(x, str) else "%s" % x

def rlabel(result):
    return '/%s' % quote_string(result) if result != None else ''

def transition(t, style):
    current, (a, args, result), next = t
    action = '%s%s%s' % (a.__name__, args, rlabel(result))
    if style == 'name':
        label = '%s' % a.__name__
    elif style == 'none':
        label = '' 
    else: # 'action'
        label = action
    return '%s -> %s [ label="%s", tooltip="%s" ]' % \
        (current, next, label, action)

def dotfile(fname, fsm, style, noStateTooltip):
    f = open(fname, 'w')
    f.write('digraph %s {\n' % os.path.basename(fname).partition('.')[0])
    f.write('\n  // Nodes\n')
    try: # FSM modules written by PyModel Analyzer have states attribute
        f.writelines([ '  %s\n' % state(n,fsm,noStateTooltip) for n in fsm.states ])    
    except: # FSM modules written by hand may not have states attribute
        nodes = set([current for (current,trans,next) in fsm.graph] 
                    + [next for (current,trans,next) in fsm.graph])
        f.writelines([ '  %s ]\n' % node(n,fsm) for n in nodes ])    
    f.write('\n  // Transitions\n')
    f.writelines([ '  %s\n' % transition(t, style) for t in fsm.graph ])
    f.write('}\n')
    f.close()
