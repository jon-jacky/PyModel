"""
Test composition with return values
"""

cases = [    
    # TestSuite
    ('Generate FSM from TestIntSuccess, ReadInt returns correct value',
     'pma TestIntSuccess'),

    ('Generate dot',
     'pmg TestIntSuccessFSM'),
    
    ('Generate SVG',
     'dotsvg TestIntSuccessFSM'),

    ('Generate FSM from TestIntWrong, ReadInt returns wrong value',
     'pma TestIntWrong'),

    ('Generate dot',
     'pmg TestIntWrongFSM'),
    
    ('Generate SVG',
     'dotsvg TestIntWrongFSM'),

    ('Generate FSM from composition, should not synchronize on different args',
     'pma -o TestIntComposeLogoutFSM TestIntSuccess TestIntWrongLogout'),

    ('Generate dot',
     'pmg TestIntComposeLogoutFSM'),
    
    ('Generate SVG',
     'dotsvg TestIntComposeLogoutFSM'),

    ('Generate FSM from composition, should not synchronize on different results',
     'pma -o TestIntComposeFSM TestIntSuccess TestIntWrong'),

    ('Generate dot',
     'pmg TestIntComposeFSM'),
    
    ('Generate SVG',
     'dotsvg TestIntComposeFSM'),
]
