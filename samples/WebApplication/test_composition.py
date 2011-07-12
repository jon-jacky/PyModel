"""
Test composition with return values
"""

cases = [    
    # TestSuite
    ('Generate FSM from TestIntSuccess, ReadInt returns correct value',
     'pma.py TestIntSuccess'),

    ('Generate dot',
     'pmg.py TestIntSuccessFSM'),
    
    ('Generate SVG',
     'dotsvg TestIntSuccessFSM'),

    ('Generate FSM from TestIntWrong, ReadInt returns wrong value',
     'pma.py TestIntWrong'),

    ('Generate dot',
     'pmg.py TestIntWrongFSM'),
    
    ('Generate SVG',
     'dotsvg TestIntWrongFSM'),

    ('Generate FSM from composition, should not synchronize on different args',
     'pma.py -o TestIntComposeLogoutFSM TestIntSuccess TestIntWrongLogout'),

    ('Generate dot',
     'pmg.py TestIntComposeLogoutFSM'),
    
    ('Generate SVG',
     'dotsvg TestIntComposeLogoutFSM'),

    ('Generate FSM from composition, should not synchronize on different results',
     'pma.py -o TestIntComposeFSM TestIntSuccess TestIntWrong'),

    ('Generate dot',
     'pmg.py TestIntComposeFSM'),
    
    ('Generate SVG',
     'dotsvg TestIntComposeFSM'),
]
