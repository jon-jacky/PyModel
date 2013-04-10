"""
oven graphics tests, showing unsafe states
"""

cases = [
    ('Generate FSM from unsafe_oven program',
     'pma unsafe_oven'),

    ('Generate dot graphics commands from generated unsafe_ovenFSM',
     'pmg unsafe_ovenFSM'),

    ('Generate SVG file from dot commands',
     'dotsvg unsafe_ovenFSM'),

    ('Generate FSM from oven program',
     'pma oven'),

    ('Generate dot graphics commands from generated ovenFSM',
     'pmg ovenFSM'),

    ('Generate SVG file from dot commands',
     'dotsvg ovenFSM'),

    # Now display svg files in a browser
]
    
