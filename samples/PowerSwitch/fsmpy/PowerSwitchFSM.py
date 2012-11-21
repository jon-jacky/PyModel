
# pma.py --exclude [PowerOff] --maxTransitions 100 PowerSwitch
# 2 states, 2 transitions, 1 accepting states, 0 unsafe states, 0 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def PowerOff(): pass
def PowerOn(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'PowerSwitch': {'power': False}},
  1 : {'PowerSwitch': {'power': True}},
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
  (1, (PowerOff, (), None), 0),
)
