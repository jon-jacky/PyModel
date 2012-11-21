
# pma.py -o TestIntComposeLogoutFSM TestIntSuccess TestIntWrongLogout
# 5 states, 4 transitions, 0 accepting states, 0 unsafe states, 0 finished and 1 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def ReadInt(): pass
def Logout(): pass
def Initialize(): pass
def Login(): pass
def UpdateInt(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'TestIntWrongLogout': (0, 0), 'TestIntSuccess': (0, 0)},
  1 : {'TestIntWrongLogout': (0, 1), 'TestIntSuccess': (0, 1)},
  2 : {'TestIntWrongLogout': (0, 2), 'TestIntSuccess': (0, 2)},
  3 : {'TestIntWrongLogout': (0, 3), 'TestIntSuccess': (0, 3)},
  4 : {'TestIntWrongLogout': (0, 4), 'TestIntSuccess': (0, 4)},
}

# initial state, accepting states, unsafe states, frontier states, deadend states

initial = 0
accepting = []
unsafe = []
frontier = []
finished = []
deadend = [4]
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (Initialize, (), None), 1),
  (1, (Login, ('VinniPuhh', 'Correct'), 'Success'), 2),
  (2, (UpdateInt, ('VinniPuhh', 1), None), 3),
  (3, (ReadInt, ('VinniPuhh',), 1), 4),
)
