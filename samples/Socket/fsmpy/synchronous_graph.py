
# pma.py --maxTransitions 100 --output synchronous_graph synchronous
# 4 states, 4 transitions, 1 accepting states, 0 unsafe states, 0 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def send_return(): pass
def send_call(): pass
def recv_call(): pass
def recv_return(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'synchronous': 0},
  1 : {'synchronous': 1},
  2 : {'synchronous': 2},
  3 : {'synchronous': 3},
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
  (0, (send_call, (), None), 1),
  (1, (send_return, (), None), 2),
  (2, (recv_call, (), None), 3),
  (3, (recv_return, (), None), 0),
)
