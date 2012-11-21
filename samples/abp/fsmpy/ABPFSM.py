
# pma.py ABP
# 5 states, 13 transitions, 3 accepting states, 0 unsafe states, 0 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def Ack(): pass
def Send(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'ABP': 0},
  1 : {'ABP': 1},
  2 : {'ABP': 2},
  3 : {'ABP': 3},
  4 : {'ABP': 4},
}

# initial state, accepting states, unsafe states, frontier states, deadend states

initial = 0
accepting = [0, 2, 4]
unsafe = []
frontier = []
finished = []
deadend = []
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (Send, (0,), None), 1),
  (0, (Ack, (1,), None), 0),
  (0, (Send, (1,), None), 0),
  (1, (Ack, (0,), None), 2),
  (1, (Send, (0,), None), 1),
  (1, (Ack, (1,), None), 1),
  (2, (Ack, (0,), None), 2),
  (2, (Send, (1,), None), 3),
  (3, (Ack, (0,), None), 3),
  (3, (Ack, (1,), None), 4),
  (3, (Send, (1,), None), 3),
  (4, (Send, (0,), None), 1),
  (4, (Ack, (1,), None), 4),
)
