
# pma.py --maxTransitions 100 DisplayFive Marquee
# 7 states, 14 transitions, 7 accepting states, 0 unsafe states, 0 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def Load(): pass
def Shift(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'Marquee': {'display': '* * * * * * * * * * * * * '}},
  1 : {'Marquee': {'display': ' * * * * * * * * * * * * *'}},
  2 : {'Marquee': {'display': 'Bye  Bye  Bye  Bye  Bye  '}},
  3 : {'Marquee': {'display': 'ye  Bye  Bye  Bye  Bye  B'}},
  4 : {'Marquee': {'display': 'e  Bye  Bye  Bye  Bye  By'}},
  5 : {'Marquee': {'display': '  Bye  Bye  Bye  Bye  Bye'}},
  6 : {'Marquee': {'display': ' Bye  Bye  Bye  Bye  Bye '}},
}

# initial state, accepting states, unsafe states, frontier states, deadend states

initial = 0
accepting = [0, 1, 2, 3, 4, 5, 6]
unsafe = []
frontier = []
finished = []
deadend = []
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (Shift, (), None), 1),
  (0, (Load, ('Bye  Bye  Bye  Bye  Bye  ',), None), 2),
  (1, (Shift, (), None), 0),
  (1, (Load, ('Bye  Bye  Bye  Bye  Bye  ',), None), 2),
  (2, (Shift, (), None), 3),
  (2, (Load, ('Bye  Bye  Bye  Bye  Bye  ',), None), 2),
  (3, (Shift, (), None), 4),
  (3, (Load, ('Bye  Bye  Bye  Bye  Bye  ',), None), 2),
  (4, (Shift, (), None), 5),
  (4, (Load, ('Bye  Bye  Bye  Bye  Bye  ',), None), 2),
  (5, (Shift, (), None), 6),
  (5, (Load, ('Bye  Bye  Bye  Bye  Bye  ',), None), 2),
  (6, (Shift, (), None), 2),
  (6, (Load, ('Bye  Bye  Bye  Bye  Bye  ',), None), 2),
)
