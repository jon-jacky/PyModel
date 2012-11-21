
# pma.py oven
# 3 states, 5 transitions, 1 accepting states, 0 unsafe states, 0 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def close(): pass
def open(): pass
def off(): pass
def on(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'oven': {'door': 'Closed', 'power': 'Off'}},
  1 : {'oven': {'door': 'Closed', 'power': 'On'}},
  2 : {'oven': {'door': 'Open', 'power': 'Off'}},
}

# initial state, accepting states, unsafe states, frontier states, deadend states

initial = 0
accepting = [0]
unsafe = []
frontier = []
finished = []
deadend = []
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (on, (), None), 1),
  (0, (open, (), None), 2),
  (1, (off, (), None), 0),
  (1, (open, (), None), 2),
  (2, (close, (), None), 0),
)
