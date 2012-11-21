
# pma.py SpeedControl PowerSwitch -o PowerSpeed
# 6 states, 12 transitions, 1 accepting states, 0 unsafe states, 0 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def PowerOff(): pass
def PowerOn(): pass
def IncrementSpeed(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'SpeedControl': 0, 'PowerSwitch': {'power': False}},
  1 : {'SpeedControl': 0, 'PowerSwitch': {'power': True}},
  2 : {'SpeedControl': 1, 'PowerSwitch': {'power': False}},
  3 : {'SpeedControl': 1, 'PowerSwitch': {'power': True}},
  4 : {'SpeedControl': 2, 'PowerSwitch': {'power': False}},
  5 : {'SpeedControl': 2, 'PowerSwitch': {'power': True}},
}

# initial state, accepting states, unsafe states, frontier states, deadend states

initial = 0
accepting = [0]
unsafe = []
frontier = []
finished = []
deadend = []
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (PowerOn, (), None), 1),
  (0, (IncrementSpeed, (), None), 2),
  (1, (IncrementSpeed, (), None), 3),
  (1, (PowerOff, (), None), 0),
  (2, (PowerOn, (), None), 3),
  (2, (IncrementSpeed, (), None), 4),
  (3, (IncrementSpeed, (), None), 5),
  (3, (PowerOff, (), None), 2),
  (4, (PowerOn, (), None), 5),
  (4, (IncrementSpeed, (), None), 0),
  (5, (IncrementSpeed, (), None), 1),
  (5, (PowerOff, (), None), 4),
)
