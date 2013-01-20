
# pma.py --maxTransitions 100 deterministic synchronous msocket
# 7 states, 8 transitions, 1 accepting states, 0 unsafe states, 0 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def send_return(): pass
def send_call(): pass
def recv_call(): pass
def recv_return(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'synchronous': 0, 'msocket': {'send_arg': '', 'recv_arg': 0, 'buffers': ''}},
  1 : {'synchronous': 1, 'msocket': {'send_arg': 'a', 'recv_arg': 0, 'buffers': ''}},
  2 : {'synchronous': 1, 'msocket': {'send_arg': 'bb', 'recv_arg': 0, 'buffers': ''}},
  3 : {'synchronous': 2, 'msocket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'a'}},
  4 : {'synchronous': 2, 'msocket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'bb'}},
  5 : {'synchronous': 3, 'msocket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'a'}},
  6 : {'synchronous': 3, 'msocket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'bb'}},
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
  (0, (send_call, ('a',), None), 1),
  (0, (send_call, ('bb',), None), 2),
  (1, (send_return, (1,), None), 3),
  (2, (send_return, (2,), None), 4),
  (3, (recv_call, (4,), None), 5),
  (4, (recv_call, (4,), None), 6),
  (5, (recv_return, ('a',), None), 0),
  (6, (recv_return, ('bb',), None), 0),
)
