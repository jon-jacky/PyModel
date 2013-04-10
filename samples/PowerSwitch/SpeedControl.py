
# pma --maxTransitions 100 --output SpeedControl SpeedControl
# 3 states, 3 transitions, 1 accepting states, 0 unsafe states, 0 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def IncrementSpeed(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'SpeedControl': 0},
  1 : {'SpeedControl': 1},
  2 : {'SpeedControl': 2},
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
  (0, (IncrementSpeed, (), None), 1),
  (1, (IncrementSpeed, (), None), 2),
  (2, (IncrementSpeed, (), None), 0),
)
