
# pma.py OneUserScenario WebModel
# 7 states, 16 transitions, 4 accepting states, 0 unsafe states, 0 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def ReadInt(): pass
def Logout(): pass
def Initialize(): pass
def Login(): pass
def UpdateInt(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'OneUserScenario': 0, 'WebModel': {'userToInt': {}, 'mode': 'Initializing', 'usersLoggedIn': []}},
  1 : {'OneUserScenario': 0, 'WebModel': {'userToInt': {}, 'mode': 'Running', 'usersLoggedIn': []}},
  2 : {'OneUserScenario': 1, 'WebModel': {'userToInt': {}, 'mode': 'Running', 'usersLoggedIn': ['VinniPuhh']}},
  3 : {'OneUserScenario': 1, 'WebModel': {'userToInt': {'VinniPuhh': 2}, 'mode': 'Running', 'usersLoggedIn': ['VinniPuhh']}},
  4 : {'OneUserScenario': 1, 'WebModel': {'userToInt': {'VinniPuhh': 1}, 'mode': 'Running', 'usersLoggedIn': ['VinniPuhh']}},
  5 : {'OneUserScenario': 0, 'WebModel': {'userToInt': {'VinniPuhh': 2}, 'mode': 'Running', 'usersLoggedIn': []}},
  6 : {'OneUserScenario': 0, 'WebModel': {'userToInt': {'VinniPuhh': 1}, 'mode': 'Running', 'usersLoggedIn': []}},
}

# initial state, accepting states, unsafe states, frontier states, deadend states

initial = 0
accepting = [0, 1, 5, 6]
unsafe = []
frontier = []
finished = []
deadend = []
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (Initialize, (), None), 1),
  (1, (Login, ('VinniPuhh', 'Correct'), 'Success'), 2),
  (2, (Logout, ('VinniPuhh',), None), 1),
  (2, (ReadInt, ('VinniPuhh',), 0), 2),
  (2, (UpdateInt, ('VinniPuhh', 2), None), 3),
  (2, (UpdateInt, ('VinniPuhh', 1), None), 4),
  (3, (Logout, ('VinniPuhh',), None), 5),
  (3, (UpdateInt, ('VinniPuhh', 2), None), 3),
  (3, (UpdateInt, ('VinniPuhh', 1), None), 4),
  (3, (ReadInt, ('VinniPuhh',), 2), 3),
  (4, (Logout, ('VinniPuhh',), None), 6),
  (4, (UpdateInt, ('VinniPuhh', 2), None), 3),
  (4, (ReadInt, ('VinniPuhh',), 1), 4),
  (4, (UpdateInt, ('VinniPuhh', 1), None), 4),
  (5, (Login, ('VinniPuhh', 'Correct'), 'Success'), 3),
  (6, (Login, ('VinniPuhh', 'Correct'), 'Success'), 4),
)
