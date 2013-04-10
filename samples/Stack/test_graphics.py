"""
Test Stack graphics
"""

cases = [
    ('Generate FSM with first 12 transitions',
     'pma Stack -m 12'),

    ('Generate dot commands',
     'pmg StackFSM'),

    ('Generate SVG file',
     'dotsvg StackFSM'),

    ('Generate dot commands for scenario FSM',
     'pmg StackOneScenario'),

    ('Generate SVG',
     'dotsvg StackOneScenario'),

    ('Explore composition of model with scenario machine, show synchronization',
     'pma Stack StackOneScenario StackDepthThree -m 6 -o StackSynchronized'),

    ('Generate dot',
     'pmg StackSynchronized'),

    ('Generate SVG',
     'dotsvg StackSynchronized')

    # Now display StackFSM.svg, StackOneScenario.svg, StackSynchronized.svg
    # in browser
]
