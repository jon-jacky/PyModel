"""
Demonstrate validation with return values
"""

cases = [    
    # TestSuite
    ('Generate FSM from allowed TestIntSuccess, ReadInt returns correct value',
     'pma TestIntSuccess'),

    ('Generate dot',
     'pmg TestIntSuccessFSM'),
    
    ('Generate SVG',
     'dotsvg TestIntSuccessFSM'),

    ('Generate FSM from forbidden TestIntWrong, ReadInt returns wrong value',
     'pma TestIntWrong'),

    ('Generate dot',
     'pmg TestIntWrongFSM'),
    
    ('Generate SVG',
     'dotsvg TestIntWrongFSM'),

    ('Compose model with allowed trace',
     'pma -o TestIntSuccessComposeFSM TestIntSuccess WebModel'),

    ('Generate dot',
     'pmg TestIntSuccessComposeFSM '),
    
    ('Generate SVG',
     'dotsvg TestIntSuccessComposeFSM '),

    ('Compose model with forbidden trace',
     'pma -o TestIntWrongComposeFSM TestIntWrong WebModel'),

    ('Generate dot',
     'pmg TestIntWrongComposeFSM'),
    
    ('Generate SVG',
     'dotsvg TestIntWrongComposeFSM'),
]
