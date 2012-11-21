
# pma.py tracemultiplexer
# 45 states, 52 transitions, 6 accepting states, 0 unsafe states, 6 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def release(): pass
def start(): pass
def finish(): pass
def call(): pass

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
  9 : {'tracemultiplexer': {'phase': ['exit', 'ready'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (0, 'listfiles', 'finish', [])], 'files': [], 'listing': []}},
  10 : {'tracemultiplexer': {'phase': ['finish', 'start'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (0, 'listfiles', 'finish', []), (1, 'openfile', 'start')], 'files': [], 'listing': []}},
  11 : {'tracemultiplexer': {'phase': ['finish', 'start'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (1, 'openfile', 'start'), (0, 'listfiles', 'finish', [])], 'files': [], 'listing': []}},
  12 : {'tracemultiplexer': {'phase': ['call', 'call'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (1, 'openfile', 'start')], 'files': ['file0'], 'listing': []}},
  13 : {'tracemultiplexer': {'phase': ['call', 'call'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (0, 'listfiles', 'start')], 'files': ['file0'], 'listing': ['file0']}},
  14 : {'tracemultiplexer': {'phase': ['start', 'finish'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (0, 'listfiles', 'start'), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': []}},
  15 : {'tracemultiplexer': {'phase': ['start', 'finish'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0'), (0, 'listfiles', 'start')], 'files': ['file0'], 'listing': []}},
  16 : {'tracemultiplexer': {'phase': ['ready', 'exit'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': []}},
  17 : {'tracemultiplexer': {'phase': ['exit', 'start'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (0, 'listfiles', 'finish', []), (1, 'openfile', 'start')], 'files': [], 'listing': []}},
  18 : {'tracemultiplexer': {'phase': ['finish', 'call'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (0, 'listfiles', 'finish', []), (1, 'openfile', 'start')], 'files': ['file0'], 'listing': []}},
  19 : {'tracemultiplexer': {'phase': ['exit', 'start'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (1, 'openfile', 'start'), (0, 'listfiles', 'finish', [])], 'files': [], 'listing': []}},
  20 : {'tracemultiplexer': {'phase': ['finish', 'call'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (1, 'openfile', 'start'), (0, 'listfiles', 'finish', [])], 'files': ['file0'], 'listing': []}},
  21 : {'tracemultiplexer': {'phase': ['call', 'finish'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': []}},
  22 : {'tracemultiplexer': {'phase': ['finish', 'call'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (0, 'listfiles', 'start'), (0, 'listfiles', 'finish', ['file0'])], 'files': ['file0'], 'listing': ['file0']}},
  23 : {'tracemultiplexer': {'phase': ['call', 'finish'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (0, 'listfiles', 'start'), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': ['file0']}},
  24 : {'tracemultiplexer': {'phase': ['start', 'exit'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (0, 'listfiles', 'start'), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': []}},
  25 : {'tracemultiplexer': {'phase': ['call', 'finish'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0'), (0, 'listfiles', 'start')], 'files': ['file0'], 'listing': ['file0']}},
  26 : {'tracemultiplexer': {'phase': ['start', 'exit'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0'), (0, 'listfiles', 'start')], 'files': ['file0'], 'listing': []}},
  27 : {'tracemultiplexer': {'phase': ['exit', 'call'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (0, 'listfiles', 'finish', []), (1, 'openfile', 'start')], 'files': ['file0'], 'listing': []}},
  28 : {'tracemultiplexer': {'phase': ['exit', 'call'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (1, 'openfile', 'start'), (0, 'listfiles', 'finish', [])], 'files': ['file0'], 'listing': []}},
  29 : {'tracemultiplexer': {'phase': ['call', 'exit'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': []}},
  30 : {'tracemultiplexer': {'phase': ['exit', 'call'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (0, 'listfiles', 'start'), (0, 'listfiles', 'finish', ['file0'])], 'files': ['file0'], 'listing': ['file0']}},
  31 : {'tracemultiplexer': {'phase': ['call', 'exit'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (0, 'listfiles', 'start'), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': ['file0']}},
  32 : {'tracemultiplexer': {'phase': ['call', 'exit'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0'), (0, 'listfiles', 'start')], 'files': ['file0'], 'listing': ['file0']}},
  33 : {'tracemultiplexer': {'phase': ['exit', 'finish'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (0, 'listfiles', 'finish', []), (1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': []}},
  34 : {'tracemultiplexer': {'phase': ['exit', 'finish'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (1, 'openfile', 'start'), (0, 'listfiles', 'finish', []), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': []}},
  35 : {'tracemultiplexer': {'phase': ['finish', 'exit'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0'), (0, 'listfiles', 'finish', [])], 'files': ['file0'], 'listing': []}},
  36 : {'tracemultiplexer': {'phase': ['exit', 'finish'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (0, 'listfiles', 'start'), (0, 'listfiles', 'finish', ['file0']), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': ['file0']}},
  37 : {'tracemultiplexer': {'phase': ['finish', 'exit'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (0, 'listfiles', 'start'), (1, 'openfile', 'finish', 'file0'), (0, 'listfiles', 'finish', ['file0'])], 'files': ['file0'], 'listing': ['file0']}},
  38 : {'tracemultiplexer': {'phase': ['finish', 'exit'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0'), (0, 'listfiles', 'start'), (0, 'listfiles', 'finish', ['file0'])], 'files': ['file0'], 'listing': ['file0']}},
  39 : {'tracemultiplexer': {'phase': ['exit', 'exit'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (0, 'listfiles', 'finish', []), (1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': []}},
  40 : {'tracemultiplexer': {'phase': ['exit', 'exit'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (1, 'openfile', 'start'), (0, 'listfiles', 'finish', []), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': []}},
  41 : {'tracemultiplexer': {'phase': ['exit', 'exit'], 'pc': [0, 0], 'log': [(0, 'listfiles', 'start'), (1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0'), (0, 'listfiles', 'finish', [])], 'files': ['file0'], 'listing': []}},
  42 : {'tracemultiplexer': {'phase': ['exit', 'exit'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (0, 'listfiles', 'start'), (0, 'listfiles', 'finish', ['file0']), (1, 'openfile', 'finish', 'file0')], 'files': ['file0'], 'listing': ['file0']}},
  43 : {'tracemultiplexer': {'phase': ['exit', 'exit'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (0, 'listfiles', 'start'), (1, 'openfile', 'finish', 'file0'), (0, 'listfiles', 'finish', ['file0'])], 'files': ['file0'], 'listing': ['file0']}},
  44 : {'tracemultiplexer': {'phase': ['exit', 'exit'], 'pc': [0, 0], 'log': [(1, 'openfile', 'start'), (1, 'openfile', 'finish', 'file0'), (0, 'listfiles', 'start'), (0, 'listfiles', 'finish', ['file0'])], 'files': ['file0'], 'listing': ['file0']}},
}

# initial state, accepting states, unsafe states, frontier states, deadend states

initial = 0
accepting = [39, 40, 41, 42, 43, 44]
unsafe = []
frontier = []
finished = [39, 40, 41, 42, 43, 44]
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
  (5, (release, (0,), None), 9),
  (5, (start, (1,), None), 10),
  (6, (finish, (0,), None), 11),
  (6, (call, (1,), None), 12),
  (7, (call, (0,), None), 13),
  (7, (finish, (1,), None), 14),
  (8, (start, (0,), None), 15),
  (8, (release, (1,), None), 16),
  (9, (start, (1,), None), 17),
  (10, (release, (0,), None), 17),
  (10, (call, (1,), None), 18),
  (11, (release, (0,), None), 19),
  (11, (call, (1,), None), 20),
  (12, (finish, (0,), None), 20),
  (12, (finish, (1,), None), 21),
  (13, (finish, (0,), None), 22),
  (13, (finish, (1,), None), 23),
  (14, (call, (0,), None), 23),
  (14, (release, (1,), None), 24),
  (15, (call, (0,), None), 25),
  (15, (release, (1,), None), 26),
  (16, (start, (0,), None), 26),
  (17, (call, (1,), None), 27),
  (18, (release, (0,), None), 27),
  (19, (call, (1,), None), 28),
  (20, (release, (0,), None), 28),
  (21, (release, (1,), None), 29),
  (22, (release, (0,), None), 30),
  (23, (release, (1,), None), 31),
  (24, (call, (0,), None), 31),
  (25, (release, (1,), None), 32),
  (26, (call, (0,), None), 32),
  (27, (finish, (1,), None), 33),
  (28, (finish, (1,), None), 34),
  (29, (finish, (0,), None), 35),
  (30, (finish, (1,), None), 36),
  (31, (finish, (0,), None), 37),
  (32, (finish, (0,), None), 38),
  (33, (release, (1,), None), 39),
  (34, (release, (1,), None), 40),
  (35, (release, (0,), None), 41),
  (36, (release, (1,), None), 42),
  (37, (release, (0,), None), 43),
  (38, (release, (0,), None), 44),
)
