
# pma.py -o TestIntSuccessComposeFSM TestIntSuccess WebModel
# 6 states, 5 transitions, 1 accepting states, 0 unsafe states, 1 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def ReadInt(): pass
def Logout(): pass
def Initialize(): pass
def Login(): pass
def UpdateInt(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'WebModel': {'userToInt': {}, 'mode': 'Initializing', 'usersLoggedIn': []}, 'TestIntSuccess': (0, 0)},
  1 : {'WebModel': {'userToInt': {}, 'mode': 'Running', 'usersLoggedIn': []}, 'TestIntSuccess': (0, 1)},
  2 : {'WebModel': {'userToInt': {}, 'mode': 'Running', 'usersLoggedIn': ['VinniPuhh']}, 'TestIntSuccess': (0, 2)},
  3 : {'WebModel': {'userToInt': {'VinniPuhh': 1}, 'mode': 'Running', 'usersLoggedIn': ['VinniPuhh']}, 'TestIntSuccess': (0, 3)},
  4 : {'WebModel': {'userToInt': {'VinniPuhh': 1}, 'mode': 'Running', 'usersLoggedIn': ['VinniPuhh']}, 'TestIntSuccess': (0, 4)},
  5 : {'WebModel': {'userToInt': {'VinniPuhh': 1}, 'mode': 'Running', 'usersLoggedIn': []}, 'TestIntSuccess': (0, 5)},
}

# initial state, accepting states, unsafe states, frontier states, deadend states

initial = 0
accepting = [5]
unsafe = []
frontier = []
finished = [5]
deadend = []
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (Initialize, (), None), 1),
  (1, (Login, ('VinniPuhh', 'Correct'), 'Success'), 2),
  (2, (UpdateInt, ('VinniPuhh', 1), None), 3),
  (3, (ReadInt, ('VinniPuhh',), 1), 4),
  (4, (Logout, ('VinniPuhh',), None), 5),
)
