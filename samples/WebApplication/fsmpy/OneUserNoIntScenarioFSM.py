
# pma.py OneUserNoIntScenario WebModel
# 3 states, 3 transitions, 2 accepting states, 0 unsafe states, 0 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def ReadInt(): pass
def Logout(): pass
def Initialize(): pass
def Login(): pass
def UpdateInt(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'OneUserNoIntScenario': 0, 'WebModel': {'userToInt': {}, 'mode': 'Initializing', 'usersLoggedIn': []}},
  1 : {'OneUserNoIntScenario': 0, 'WebModel': {'userToInt': {}, 'mode': 'Running', 'usersLoggedIn': []}},
  2 : {'OneUserNoIntScenario': 1, 'WebModel': {'userToInt': {}, 'mode': 'Running', 'usersLoggedIn': ['VinniPuhh']}},
}

# initial state, accepting states, unsafe states, frontier states, deadend states

initial = 0
accepting = [0, 1]
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
)
