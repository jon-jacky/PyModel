
# pma.py --action send_close --action recv_close --maxTransitions 100 --output NoBlockScenario_a NoBlockScenario
# 1 states, 2 transitions, 1 accepting states, 0 unsafe states, 0 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def send_close(): pass
def recv_close(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'NoBlockScenario': 0},
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
  (0, (recv_close, (), None), 0),
  (0, (send_close, (), None), 0),
)
