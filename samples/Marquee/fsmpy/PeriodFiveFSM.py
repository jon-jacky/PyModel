
# pma.py --maxTransitions 100 --output PeriodFiveFSM Marquee DisplayFive LoadFirst
# 6 states, 6 transitions, 6 accepting states, 0 unsafe states, 0 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def Load(): pass
def Shift(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'Marquee': {'display': '* * * * * * * * * * * * * '}, 'LoadFirst': 0},
  1 : {'LoadFirst': 1, 'Marquee': {'display': 'Bye  Bye  Bye  Bye  Bye  '}},
  2 : {'LoadFirst': 1, 'Marquee': {'display': 'ye  Bye  Bye  Bye  Bye  B'}},
  3 : {'LoadFirst': 1, 'Marquee': {'display': 'e  Bye  Bye  Bye  Bye  By'}},
  4 : {'LoadFirst': 1, 'Marquee': {'display': '  Bye  Bye  Bye  Bye  Bye'}},
  5 : {'LoadFirst': 1, 'Marquee': {'display': ' Bye  Bye  Bye  Bye  Bye '}},
}

# initial state, accepting states, unsafe states, frontier states, deadend states

initial = 0
accepting = [0, 1, 2, 3, 4, 5]
unsafe = []
frontier = []
finished = []
deadend = []
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (Load, ('Bye  Bye  Bye  Bye  Bye  ',), None), 1),
  (1, (Shift, (), None), 2),
  (2, (Shift, (), None), 3),
  (3, (Shift, (), None), 4),
  (4, (Shift, (), None), 5),
  (5, (Shift, (), None), 1),
)
