
# pma.py -o ValidateScenarios Scenarios Stack
# 11 states, 7 transitions, 1 accepting states, 0 unsafe states, 1 finished and 3 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def Push(): pass
def Pop(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'Scenarios': (0, 0), 'Stack': {'stack': []}},
  1 : {'Scenarios': (0, 1), 'Stack': {'stack': [1]}},
  2 : {'Scenarios': (0, 2), 'Stack': {'stack': [2, 1]}},
  3 : {'Scenarios': (0, 3), 'Stack': {'stack': [1]}},
  4 : {'Scenarios': (0, 4), 'Stack': {'stack': []}},
  5 : {'Scenarios': (1, 0), 'Stack': {'stack': []}},
  6 : {'Scenarios': (1, 1), 'Stack': {'stack': [1]}},
  7 : {'Scenarios': (1, 2), 'Stack': {'stack': [2, 1]}},
  8 : {'Scenarios': (2, 0), 'Stack': {'stack': []}},
  9 : {'Scenarios': (2, 1), 'Stack': {'stack': [1]}},
  10 : {'Scenarios': (3, 0), 'Stack': {'stack': []}},
}

# initial state, accepting states, unsafe states, frontier states, deadend states

initial = 0
accepting = [4]
unsafe = []
frontier = []
finished = [4]
deadend = [7, 9, 10]
runstarts = [0, 5, 8, 10]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (Push, (1,), None), 1),
  (1, (Push, (2,), None), 2),
  (2, (Pop, (2,), None), 3),
  (3, (Pop, (1,), None), 4),
  (5, (Push, (1,), None), 6),
  (6, (Push, (2,), None), 7),
  (8, (Push, (1,), None), 9),
)
