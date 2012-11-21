
# pma.py Marquee
# 2 states, 2 transitions, 2 accepting states, 0 unsafe states, 0 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def Shift(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'Marquee': {'display': '* * * * * * * * * * * * * '}},
  1 : {'Marquee': {'display': ' * * * * * * * * * * * * *'}},
}

# initial state, accepting states, unsafe states, frontier states, deadend states

initial = 0
accepting = [0, 1]
unsafe = []
frontier = []
finished = []
deadend = []
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (Shift, (), None), 1),
  (1, (Shift, (), None), 0),
)
