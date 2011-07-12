"""
Scenario control for Marquee, load once at the beginning then keep shifting
"""

from Marquee import Load, Shift

initial = 0
accepting = (0,1)

graph = ((0, (Load, (), None), 1),   # empty args here, match any pattern
         (1, (Shift, (), None), 1))

