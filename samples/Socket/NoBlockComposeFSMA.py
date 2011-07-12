
# pma.py -o NoBlockComposeFSMA Socket NoBlockScenario SocketSendA
# 14 states, 18 transitions, 9 accepting states, 3 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def send_return(): pass
def send_call(): pass
def recv_close(): pass
def send_close(): pass
def recv_call(): pass
def send_exception(): pass
def recv_return(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'NoBlockScenario': 0, 'Socket': {'exception': '', 'recv_closed': False, 'send_arg': '', 'recv_arg': 0, 'send_closed': False, 'buffers': ''}},
  1 : {'NoBlockScenario': 0, 'Socket': {'exception': '', 'recv_closed': True, 'send_arg': '', 'recv_arg': 0, 'send_closed': False, 'buffers': ''}},
  2 : {'NoBlockScenario': 0, 'Socket': {'exception': '', 'recv_closed': False, 'send_arg': '', 'recv_arg': 0, 'send_closed': True, 'buffers': ''}},
  3 : {'NoBlockScenario': 1, 'Socket': {'exception': '', 'recv_closed': False, 'send_arg': 'a', 'recv_arg': 0, 'send_closed': False, 'buffers': ''}},
  4 : {'NoBlockScenario': 0, 'Socket': {'exception': '', 'recv_closed': True, 'send_arg': '', 'recv_arg': 0, 'send_closed': True, 'buffers': ''}},
  5 : {'NoBlockScenario': 1, 'Socket': {'exception': '', 'recv_closed': True, 'send_arg': 'a', 'recv_arg': 0, 'send_closed': False, 'buffers': ''}},
  6 : {'NoBlockScenario': 2, 'Socket': {'exception': '', 'recv_closed': False, 'send_arg': '', 'recv_arg': 0, 'send_closed': False, 'buffers': 'a'}},
  7 : {'NoBlockScenario': 2, 'Socket': {'exception': '', 'recv_closed': True, 'send_arg': '', 'recv_arg': 0, 'send_closed': False, 'buffers': 'a'}},
  8 : {'NoBlockScenario': 3, 'Socket': {'exception': '', 'recv_closed': False, 'send_arg': '', 'recv_arg': 4, 'send_closed': False, 'buffers': 'a'}},
  9 : {'NoBlockScenario': 2, 'Socket': {'exception': '', 'recv_closed': False, 'send_arg': '', 'recv_arg': 0, 'send_closed': True, 'buffers': 'a'}},
  10 : {'NoBlockScenario': 2, 'Socket': {'exception': '', 'recv_closed': True, 'send_arg': '', 'recv_arg': 0, 'send_closed': True, 'buffers': 'a'}},
  11 : {'NoBlockScenario': 3, 'Socket': {'exception': '', 'recv_closed': False, 'send_arg': '', 'recv_arg': 4, 'send_closed': True, 'buffers': 'a'}},
  12 : {'NoBlockScenario': 0, 'Socket': {'exception': '', 'recv_closed': False, 'send_arg': '', 'recv_arg': 0, 'send_closed': True, 'buffers': 'a'}},
  13 : {'NoBlockScenario': 0, 'Socket': {'exception': '', 'recv_closed': True, 'send_arg': '', 'recv_arg': 0, 'send_closed': True, 'buffers': 'a'}},
}

# initial state, accepting states, frontier states, deadend states

initial = 0
accepting = [0, 1, 2, 4, 7, 9, 10, 12, 13]
frontier = []
finished = [4, 10, 13]
deadend = []
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (recv_close, (), None), 1),
  (0, (send_close, (), None), 2),
  (0, (send_call, ('a',), None), 3),
  (1, (send_close, (), None), 4),
  (1, (send_call, ('a',), None), 5),
  (2, (recv_close, (), None), 4),
  (3, (send_return, (1,), None), 6),
  (5, (send_return, (1,), None), 7),
  (6, (recv_close, (), None), 7),
  (6, (recv_call, (4,), None), 8),
  (6, (send_close, (), None), 9),
  (7, (send_close, (), None), 10),
  (8, (recv_return, (1,), 'a'), 0),
  (9, (recv_close, (), None), 10),
  (9, (recv_call, (4,), None), 11),
  (11, (recv_return, (0,), ''), 12),
  (11, (recv_return, (1,), 'a'), 2),
  (12, (recv_close, (), None), 13),
)
