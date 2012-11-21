
# pma.py Scenarios
# 20 states, 16 transitions, 4 accepting states, 0 unsafe states, 4 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def Push(): pass
def Pop(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'Scenarios': (0, 0)},
  1 : {'Scenarios': (0, 1)},
  2 : {'Scenarios': (0, 2)},
  3 : {'Scenarios': (0, 3)},
  4 : {'Scenarios': (0, 4)},
  5 : {'Scenarios': (1, 0)},
  6 : {'Scenarios': (1, 1)},
  7 : {'Scenarios': (1, 2)},
  8 : {'Scenarios': (1, 3)},
  9 : {'Scenarios': (1, 4)},
  10 : {'Scenarios': (2, 0)},
  11 : {'Scenarios': (2, 1)},
  12 : {'Scenarios': (2, 2)},
  13 : {'Scenarios': (2, 3)},
  14 : {'Scenarios': (2, 4)},
  15 : {'Scenarios': (3, 0)},
  16 : {'Scenarios': (3, 1)},
  17 : {'Scenarios': (3, 2)},
  18 : {'Scenarios': (3, 3)},
  19 : {'Scenarios': (3, 4)},
}

# initial state, accepting states, unsafe states, frontier states, deadend states

initial = 0
accepting = [4, 9, 14, 19]
unsafe = []
frontier = []
finished = [4, 9, 14, 19]
deadend = []
runstarts = [0, 5, 10, 15]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (Push, (1,), None), 1),
  (1, (Push, (2,), None), 2),
  (2, (Pop, (2,), None), 3),
  (3, (Pop, (1,), None), 4),
  (5, (Push, (1,), None), 6),
  (6, (Push, (2,), None), 7),
  (7, (Pop, (1,), None), 8),
  (8, (Pop, (2,), None), 9),
  (10, (Push, (1,), None), 11),
  (11, (Push, (3,), None), 12),
  (12, (Pop, (3,), None), 13),
  (13, (Pop, (1,), None), 14),
  (15, (Pop, (2,), None), 16),
  (16, (Pop, (1,), None), 17),
  (17, (Push, (1,), None), 18),
  (18, (Push, (2,), None), 19),
)
