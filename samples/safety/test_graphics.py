"""
oven graphics tests, showing unsafe states
"""

cases = [
    ('Generate FSM from unsafe_oven program',
     'pma.py unsafe_oven'),

    ('Generate dot graphics commands from generated unsafe_ovenFSM',
     'pmg.py unsafe_ovenFSM'),

    ('Generate SVG file from dot commands',
     'dotsvg unsafe_ovenFSM'),

    ('Generate FSM from oven program',
     'pma.py oven'),

    ('Generate dot graphics commands from generated ovenFSM',
     'pmg.py ovenFSM'),

    ('Generate SVG file from dot commands',
     'dotsvg ovenFSM'),

    # Now display svg files in a browser
]
    
