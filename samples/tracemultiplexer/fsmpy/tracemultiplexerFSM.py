
# pma.py --maxTransitions 100 tracemultiplexer
# 37 states, 36 transitions, 6 accepting states, 0 unsafe states, 6 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def start(): pass
def finish(): pass
def call(): pass
def exit(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'tracemultiplexer': {'phase': ['ready', 'ready'], 'pc': [0, 0], 'log': [], 'files': [], 'listing': []}},
  1 : {'tracemultiplexer': {'phase': ['start', 'ready'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start')], 'files': [], 'listing': []}},
  2 : {'tracemultiplexer': {'phase': ['ready', 'start'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start')], 'files': [], 'listing': []}},
  3 : {'tracemultiplexer': {'phase': ['call', 'ready'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start')], 'files': [], 'listing': []}},
  4 : {'tracemultiplexer': {'phase': ['ready', 'call'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start')], 'files': ['file0'], 'listing': []}},
  5 : {'tracemultiplexer': {'phase': ['finish', 'ready'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (0, 'listfiles', 'finish', [])], 'files': [], 'listing': []}},
  6 : {'tracemultiplexer': {'phase': ['call', 'start'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (1, 'openfile', 'start')], 'files': [], 'listing': []}},
  7 : {'tracemultiplexer': {'phase': ['start', 'call'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (0, 'listfiles', 'start')], 'files': ['file0'], 'listing': []}},
  8 : {'tracemultiplexer': {'phase': ['ready', 'finish'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': []}},
  9 : {'tracemultiplexer': {'phase': ['done', 'ready'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (0, 'listfiles', 'finish', [])], 'files': [], 'listing': []}},
  10 : {'tracemultiplexer': {'phase': ['call', 'call'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (1, 'openfile', 'start')], 'files': ['file0'], 'listing': []}},
  11 : {'tracemultiplexer': {'phase': ['call', 'call'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (0, 'listfiles', 'start')], 'files': ['file0'], 'listing': ['file0']}},
  12 : {'tracemultiplexer': {'phase': ['ready', 'done'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': []}},
  13 : {'tracemultiplexer': {'phase': ['done', 'start'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (0, 'listfiles', 'finish', []), (1, 'openfile', 'start')], 'files': [], 'listing': []}},
  14 : {'tracemultiplexer': {'phase': ['finish', 'call'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (1, 'openfile', 'start'), (0, 'listfiles', 'finish', [])], 'files': ['file0'], 'listing': []}},
  15 : {'tracemultiplexer': {'phase': ['call', 'finish'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': []}},
  16 : {'tracemultiplexer': {'phase': ['finish', 'call'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (0, 'listfiles', 'start'), (0, 'listfiles', 'finish', ['file0'])], 'files': ['file0'], 'listing': ['file0']}},
  17 : {'tracemultiplexer': {'phase': ['call', 'finish'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (0, 'listfiles', 'start'), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': ['file0']}},
  18 : {'tracemultiplexer': {'phase': ['start', 'done'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0'), (0, 'listfiles', 'start')], 'files': ['file0'], 'listing': []}},
  19 : {'tracemultiplexer': {'phase': ['done', 'call'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (0, 'listfiles', 'finish', []), (1, 'openfile', 'start')], 'files': ['file0'], 'listing': []}},
  20 : {'tracemultiplexer': {'phase': ['done', 'call'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (1, 'openfile', 'start'), (0, 'listfiles', 'finish', [])], 'files': ['file0'], 'listing': []}},
  21 : {'tracemultiplexer': {'phase': ['call', 'done'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': []}},
  22 : {'tracemultiplexer': {'phase': ['done', 'call'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (0, 'listfiles', 'start'), (0, 'listfiles', 'finish', ['file0'])], 'files': ['file0'], 'listing': ['file0']}},
  23 : {'tracemultiplexer': {'phase': ['call', 'done'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (0, 'listfiles', 'start'), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': ['file0']}},
  24 : {'tracemultiplexer': {'phase': ['call', 'done'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0'), (0, 'listfiles', 'start')], 'files': ['file0'], 'listing': ['file0']}},
  25 : {'tracemultiplexer': {'phase': ['done', 'finish'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (0, 'listfiles', 'finish', []), (1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': []}},
  26 : {'tracemultiplexer': {'phase': ['done', 'finish'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (1, 'openfile', 'start'), (0, 'listfiles', 'finish', []), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': []}},
  27 : {'tracemultiplexer': {'phase': ['finish', 'done'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0'), (0, 'listfiles', 'finish', [])], 'files': ['file0'], 'listing': []}},
  28 : {'tracemultiplexer': {'phase': ['done', 'finish'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (0, 'listfiles', 'start'), (0, 'listfiles', 'finish', ['file0']), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': ['file0']}},
  29 : {'tracemultiplexer': {'phase': ['finish', 'done'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (0, 'listfiles', 'start'), (1, 'openfile', 'finish', 'file0'), (0, 'listfiles', 'finish', ['file0'])], 'files': ['file0'], 'listing': ['file0']}},
  30 : {'tracemultiplexer': {'phase': ['finish', 'done'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0'), (0, 'listfiles', 'start'), (0, 'listfiles', 'finish', ['file0'])], 'files': ['file0'], 'listing': ['file0']}},
  31 : {'tracemultiplexer': {'phase': ['done', 'done'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (0, 'listfiles', 'finish', []), (1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': []}},
  32 : {'tracemultiplexer': {'phase': ['done', 'done'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (1, 'openfile', 'start'), (0, 'listfiles', 'finish', []), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': []}},
  33 : {'tracemultiplexer': {'phase': ['done', 'done'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0'), (0, 'listfiles', 'finish', [])], 'files': ['file0'], 'listing': []}},
  34 : {'tracemultiplexer': {'phase': ['done', 'done'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (0, 'listfiles', 'start'), (0, 'listfiles', 'finish', ['file0']), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': ['file0']}},
  35 : {'tracemultiplexer': {'phase': ['done', 'done'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (0, 'listfiles', 'start'), (1, 'openfile', 'finish', 'file0'), (0, 'listfiles', 'finish', ['file0'])], 'files': ['file0'], 'listing': ['file0']}},
  36 : {'tracemultiplexer': {'phase': ['done', 'done'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0'), (0, 'listfiles', 'start'), (0, 'listfiles', 'finish', ['file0'])], 'files': ['file0'], 'listing': ['file0']}},
}

# initial state, accepting states, unsafe states, frontier states, deadend states

initial = 0
accepting = [31, 32, 33, 34, 35, 36]
unsafe = []
frontier = []
finished = [31, 32, 33, 34, 35, 36]
deadend = []
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (start, (0,), None), 1),
  (0, (start, (1,), None), 2),
  (1, (call, (0,), None), 3),
  (2, (call, (1,), None), 4),
  (3, (finish, (0,), None), 5),
  (3, (start, (1,), None), 6),
  (4, (start, (0,), None), 7),
  (4, (finish, (1,), None), 8),
  (5, (exit, (0,), None), 9),
  (6, (call, (1,), None), 10),
  (7, (call, (0,), None), 11),
  (8, (exit, (1,), None), 12),
  (9, (start, (1,), None), 13),
  (10, (finish, (0,), None), 14),
  (10, (finish, (1,), None), 15),
  (11, (finish, (0,), None), 16),
  (11, (finish, (1,), None), 17),
  (12, (start, (0,), None), 18),
  (13, (call, (1,), None), 19),
  (14, (exit, (0,), None), 20),
  (15, (exit, (1,), None), 21),
  (16, (exit, (0,), None), 22),
  (17, (exit, (1,), None), 23),
  (18, (call, (0,), None), 24),
  (19, (finish, (1,), None), 25),
  (20, (finish, (1,), None), 26),
  (21, (finish, (0,), None), 27),
  (22, (finish, (1,), None), 28),
  (23, (finish, (0,), None), 29),
  (24, (finish, (0,), None), 30),
  (25, (exit, (1,), None), 31),
  (26, (exit, (1,), None), 32),
  (27, (exit, (0,), None), 33),
  (28, (exit, (1,), None), 34),
  (29, (exit, (0,), None), 35),
  (30, (exit, (0,), None), 36),
)
