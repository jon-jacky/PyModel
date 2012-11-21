
# pma.py --exclude PowerOff --maxTransitions 100 --output PowerSwitchExclude PowerSwitch
# 2 states, 1 transitions, 1 accepting states, 0 unsafe states, 0 finished and 1 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

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
deadend = [1]
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (PowerOn, (), None), 1),
)
