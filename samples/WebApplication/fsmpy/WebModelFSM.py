
# pma.py WebModel -m 50
# 21 states, 50 transitions, 5 accepting states, 0 unsafe states, 0 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def Initialize(): pass
def ReadInt(): pass
def Login(): pass
def Logout(): pass
def UpdateInt(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'WebModel': {'userToInt': {}, 'mode': 'Initializing', 'usersLoggedIn': []}},
  1 : {'WebModel': {'userToInt': {}, 'mode': 'Running', 'usersLoggedIn': []}},
  2 : {'WebModel': {'userToInt': {}, 'mode': 'Running', 'usersLoggedIn': ['OleBrumm']}},
  3 : {'WebModel': {'userToInt': {}, 'mode': 'Running', 'usersLoggedIn': ['VinniPuhh']}},
  4 : {'WebModel': {'userToInt': {'OleBrumm': 1}, 'mode': 'Running', 'usersLoggedIn': ['OleBrumm']}},
  5 : {'WebModel': {'userToInt': {}, 'mode': 'Running', 'usersLoggedIn': ['OleBrumm', 'VinniPuhh']}},
  6 : {'WebModel': {'userToInt': {'OleBrumm': 2}, 'mode': 'Running', 'usersLoggedIn': ['OleBrumm']}},
  7 : {'WebModel': {'userToInt': {}, 'mode': 'Running', 'usersLoggedIn': ['VinniPuhh', 'OleBrumm']}},
  8 : {'WebModel': {'userToInt': {'VinniPuhh': 2}, 'mode': 'Running', 'usersLoggedIn': ['VinniPuhh']}},
  9 : {'WebModel': {'userToInt': {'VinniPuhh': 1}, 'mode': 'Running', 'usersLoggedIn': ['VinniPuhh']}},
  10 : {'WebModel': {'userToInt': {'OleBrumm': 1}, 'mode': 'Running', 'usersLoggedIn': ['OleBrumm', 'VinniPuhh']}},
  11 : {'WebModel': {'userToInt': {'OleBrumm': 1}, 'mode': 'Running', 'usersLoggedIn': []}},
  12 : {'WebModel': {'userToInt': {'VinniPuhh': 2}, 'mode': 'Running', 'usersLoggedIn': ['OleBrumm', 'VinniPuhh']}},
  13 : {'WebModel': {'userToInt': {'VinniPuhh': 1}, 'mode': 'Running', 'usersLoggedIn': ['OleBrumm', 'VinniPuhh']}},
  14 : {'WebModel': {'userToInt': {'OleBrumm': 2}, 'mode': 'Running', 'usersLoggedIn': ['OleBrumm', 'VinniPuhh']}},
  15 : {'WebModel': {'userToInt': {'OleBrumm': 2}, 'mode': 'Running', 'usersLoggedIn': []}},
  16 : {'WebModel': {'userToInt': {'OleBrumm': 1}, 'mode': 'Running', 'usersLoggedIn': ['VinniPuhh', 'OleBrumm']}},
  17 : {'WebModel': {'userToInt': {'VinniPuhh': 2}, 'mode': 'Running', 'usersLoggedIn': ['VinniPuhh', 'OleBrumm']}},
  18 : {'WebModel': {'userToInt': {'VinniPuhh': 1}, 'mode': 'Running', 'usersLoggedIn': ['VinniPuhh', 'OleBrumm']}},
  19 : {'WebModel': {'userToInt': {'OleBrumm': 2}, 'mode': 'Running', 'usersLoggedIn': ['VinniPuhh', 'OleBrumm']}},
  20 : {'WebModel': {'userToInt': {'VinniPuhh': 2}, 'mode': 'Running', 'usersLoggedIn': []}},
}

# initial state, accepting states, unsafe states, frontier states, deadend states

initial = 0
accepting = [0, 1, 11, 15, 20]
unsafe = []
frontier = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
finished = []
deadend = []
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (Initialize, (), None), 1),
  (1, (Login, ('OleBrumm', 'Incorrect'), 'Failure'), 1),
  (1, (Login, ('VinniPuhh', 'Incorrect'), 'Failure'), 1),
  (1, (Login, ('OleBrumm', 'Correct'), 'Success'), 2),
  (1, (Login, ('VinniPuhh', 'Correct'), 'Success'), 3),
  (2, (UpdateInt, ('OleBrumm', 1), None), 4),
  (2, (Login, ('VinniPuhh', 'Correct'), 'Success'), 5),
  (2, (Login, ('VinniPuhh', 'Incorrect'), 'Failure'), 2),
  (2, (Logout, ('OleBrumm',), None), 1),
  (2, (ReadInt, ('OleBrumm',), 0), 2),
  (2, (UpdateInt, ('OleBrumm', 2), None), 6),
  (3, (Logout, ('VinniPuhh',), None), 1),
  (3, (Login, ('OleBrumm', 'Correct'), 'Success'), 7),
  (3, (ReadInt, ('VinniPuhh',), 0), 3),
  (3, (UpdateInt, ('VinniPuhh', 2), None), 8),
  (3, (Login, ('OleBrumm', 'Incorrect'), 'Failure'), 3),
  (3, (UpdateInt, ('VinniPuhh', 1), None), 9),
  (4, (UpdateInt, ('OleBrumm', 1), None), 4),
  (4, (Login, ('VinniPuhh', 'Correct'), 'Success'), 10),
  (4, (Login, ('VinniPuhh', 'Incorrect'), 'Failure'), 4),
  (4, (ReadInt, ('OleBrumm',), 1), 4),
  (4, (Logout, ('OleBrumm',), None), 11),
  (4, (UpdateInt, ('OleBrumm', 2), None), 6),
  (5, (Logout, ('VinniPuhh',), None), 2),
  (5, (UpdateInt, ('OleBrumm', 1), None), 10),
  (5, (ReadInt, ('VinniPuhh',), 0), 5),
  (5, (UpdateInt, ('VinniPuhh', 2), None), 12),
  (5, (UpdateInt, ('VinniPuhh', 1), None), 13),
  (5, (Logout, ('OleBrumm',), None), 3),
  (5, (ReadInt, ('OleBrumm',), 0), 5),
  (5, (UpdateInt, ('OleBrumm', 2), None), 14),
  (6, (UpdateInt, ('OleBrumm', 1), None), 4),
  (6, (Login, ('VinniPuhh', 'Correct'), 'Success'), 14),
  (6, (ReadInt, ('OleBrumm',), 2), 6),
  (6, (Login, ('VinniPuhh', 'Incorrect'), 'Failure'), 6),
  (6, (Logout, ('OleBrumm',), None), 15),
  (6, (UpdateInt, ('OleBrumm', 2), None), 6),
  (7, (Logout, ('VinniPuhh',), None), 2),
  (7, (UpdateInt, ('OleBrumm', 1), None), 16),
  (7, (ReadInt, ('VinniPuhh',), 0), 7),
  (7, (UpdateInt, ('VinniPuhh', 2), None), 17),
  (7, (UpdateInt, ('VinniPuhh', 1), None), 18),
  (7, (Logout, ('OleBrumm',), None), 3),
  (7, (ReadInt, ('OleBrumm',), 0), 7),
  (7, (UpdateInt, ('OleBrumm', 2), None), 19),
  (8, (Logout, ('VinniPuhh',), None), 20),
  (8, (Login, ('OleBrumm', 'Correct'), 'Success'), 17),
  (8, (UpdateInt, ('VinniPuhh', 2), None), 8),
  (8, (Login, ('OleBrumm', 'Incorrect'), 'Failure'), 8),
  (8, (UpdateInt, ('VinniPuhh', 1), None), 9),
)
