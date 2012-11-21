
# pma.py unsafe_oven
# 4 states, 8 transitions, 1 accepting states, 1 unsafe states, 0 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def close(): pass
def open(): pass
def off(): pass
def on(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'unsafe_oven': {'door': 'Closed', 'power': 'Off'}},
  1 : {'unsafe_oven': {'door': 'Closed', 'power': 'On'}},
  2 : {'unsafe_oven': {'door': 'Open', 'power': 'Off'}},
  3 : {'unsafe_oven': {'door': 'Open', 'power': 'On'}},
}

# initial state, accepting states, unsafe states, frontier states, deadend states

initial = 0
accepting = [0]
unsafe = [3]
frontier = []
finished = []
deadend = []
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (on, (), None), 1),
  (0, (open, (), None), 2),
  (1, (off, (), None), 0),
  (1, (open, (), None), 3),
  (2, (close, (), None), 0),
  (2, (on, (), None), 3),
  (3, (close, (), None), 1),
  (3, (off, (), None), 2),
)
