"""
Test Stack graphics
"""

cases = [
    ('Generate FSM with first 12 transitions',
     'pma.py Stack -m 12'),

    ('Generate dot commands',
     'pmg.py StackFSM'),

    ('Generate SVG file',
     'dotsvg StackFSM'),

    ('Generate dot commands for scenario FSM',
     'pmg.py StackOneScenario'),

    ('Generate SVG',
     'dotsvg StackOneScenario'),

    ('Explore composition of model with scenario machine, show synchronization',
     'pma.py Stack StackOneScenario StackDepthThree -m 6 -o StackSynchronized'),

    ('Generate dot',
     'pmg.py StackSynchronized'),

    ('Generate SVG',
     'dotsvg StackSynchronized')

    # Now display StackFSM.svg, StackOneScenario.svg, StackSynchronized.svg
    # in browser
]
