"""
PowerSwitch graphics tests
"""

cases = [
    ('Generate FSM from PowerSwitch model program',
     'pma.py PowerSwitch'),

    ('Generate dot graphics commands from generated PowerSwitchFSM',
     'pmg.py PowerSwitchFSM'),

    ('Generate SVG file from dot commands',
     'dotsvg PowerSwitchFSM'),

    ('Generate dot commands from SpeedControl FSM',
     'pmg.py SpeedControl'),

    ('Generate SVG file from dot commands',
     'dotsvg SpeedControl'),

    ('Generate FSM from composition of PowerSwitch and SpeedControl, show interleaving',
     'pma.py SpeedControl PowerSwitch -o PowerSpeed'),
     
    ('Generate dot commands from composed FSM',
     'pmg.py PowerSpeed'),

    ('Generate SVG from dot',
     'dotsvg PowerSpeed')

    # Now display PowerSwitch.svg, SpeedControl.svg and PowerSpeed.svg 
    # in three browser tabs
]
    
