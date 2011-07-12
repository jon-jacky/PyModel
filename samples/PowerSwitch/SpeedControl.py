"""
SpeedControl defined by FSM, no shared actions with PowerSwitch
"""

def IncrementSpeed(): pass

cleanup = (IncrementSpeed,)

initial = 0
accepting = (0,)

graph = ((0, (IncrementSpeed, (), None), 1),
         (1, (IncrementSpeed, (), None), 2),
         (2, (IncrementSpeed, (), None), 0))
