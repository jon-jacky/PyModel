
# pma.py Stack -m 12
# 10 states, 12 transitions, 10 accepting states, 0 unsafe states, 0 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def Push(): pass
def Pop(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'Stack': {'stack': []}},
  1 : {'Stack': {'stack': [2]}},
  2 : {'Stack': {'stack': [1]}},
  3 : {'Stack': {'stack': [2, 2]}},
  4 : {'Stack': {'stack': [1, 2]}},
  5 : {'Stack': {'stack': [2, 1]}},
  6 : {'Stack': {'stack': [1, 1]}},
  7 : {'Stack': {'stack': [2, 2, 2]}},
  8 : {'Stack': {'stack': [1, 2, 2]}},
  9 : {'Stack': {'stack': [2, 1, 2]}},
}

# initial state, accepting states, unsafe states, frontier states, deadend states

initial = 0
accepting = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
unsafe = []
frontier = [4, 5, 6, 7, 8, 9]
finished = []
deadend = []
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (Push, (2,), None), 1),
  (0, (Push, (1,), None), 2),
  (1, (Pop, (2,), None), 0),
  (1, (Push, (2,), None), 3),
  (1, (Push, (1,), None), 4),
  (2, (Push, (2,), None), 5),
  (2, (Push, (1,), None), 6),
  (2, (Pop, (1,), None), 0),
  (3, (Pop, (2,), None), 1),
  (3, (Push, (2,), None), 7),
  (3, (Push, (1,), None), 8),
  (4, (Push, (2,), None), 9),
)
