
# pma.py --maxTransitions 100 TestIntFailure
# 7 states, 6 transitions, 1 accepting states, 0 unsafe states, 1 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def Initialize(): pass
def ReadInt(): pass
def Login(): pass
def Logout(): pass
def UpdateInt(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'TestIntFailure': (0, 0)},
  1 : {'TestIntFailure': (0, 1)},
  2 : {'TestIntFailure': (0, 2)},
  3 : {'TestIntFailure': (0, 3)},
  4 : {'TestIntFailure': (0, 4)},
  5 : {'TestIntFailure': (0, 5)},
  6 : {'TestIntFailure': (0, 6)},
}

# initial state, accepting states, unsafe states, frontier states, deadend states

initial = 0
accepting = [6]
unsafe = []
frontier = []
finished = [6]
deadend = []
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (Initialize, (), None), 1),
  (1, (Login, ('VinniPuhh', 'Correct'), 'Success'), 2),
  (2, (UpdateInt, ('VinniPuhh', 1), None), 3),
  (3, (Logout, ('VinniPuhh',), None), 4),
  (4, (Login, ('VinniPuhh', 'Correct'), 'Success'), 5),
  (5, (ReadInt, ('VinniPuhh',), 1), 6),
)
