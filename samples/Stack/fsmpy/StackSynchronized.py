
# pma.py Stack StackOneScenario StackDepthThree -m 6 -o StackSynchronized
# 4 states, 6 transitions, 4 accepting states, 0 unsafe states, 0 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def Push(): pass
def Pop(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'StackOneScenario': 0, 'Stack': {'stack': []}},
  1 : {'StackOneScenario': 0, 'Stack': {'stack': [1]}},
  2 : {'StackOneScenario': 0, 'Stack': {'stack': [1, 1]}},
  3 : {'StackOneScenario': 0, 'Stack': {'stack': [1, 1, 1]}},
}

# initial state, accepting states, unsafe states, frontier states, deadend states

initial = 0
accepting = [0, 1, 2, 3]
unsafe = []
frontier = []
finished = []
deadend = []
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (Push, (1,), None), 1),
  (1, (Push, (1,), None), 2),
  (1, (Pop, (1,), None), 0),
  (2, (Push, (1,), None), 3),
  (2, (Pop, (1,), None), 1),
  (3, (Pop, (1,), None), 2),
)
