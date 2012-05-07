"""
oven graphics tests, showing unsafe states
"""

cases = [
    ('Generate FSM from unsafe_oven program',
     'pma.py unsafe_oven'),

    ('Generate dot graphics commands from generated PowerSwitchFSM',
     'pmg.py unsafe_ovenFSM'),

    ('Generate SVG file from dot commands',
     'dotsvg unsafe_ovenFSM'),

    # Now display unsafe_ovenFSM.svg in a browser
]
    
