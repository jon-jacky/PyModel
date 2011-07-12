"""
Demonstrate validation with return values
"""

cases = [    
    # TestSuite
    ('Generate FSM from allowed TestIntSuccess, ReadInt returns correct value',
     'pma.py TestIntSuccess'),

    ('Generate dot',
     'pmg.py TestIntSuccessFSM'),
    
    ('Generate SVG',
     'dotsvg TestIntSuccessFSM'),

    ('Generate FSM from forbidden TestIntWrong, ReadInt returns wrong value',
     'pma.py TestIntWrong'),

    ('Generate dot',
     'pmg.py TestIntWrongFSM'),
    
    ('Generate SVG',
     'dotsvg TestIntWrongFSM'),

    ('Compose model with allowed trace',
     'pma.py -o TestIntSuccessComposeFSM TestIntSuccess WebModel'),

    ('Generate dot',
     'pmg.py TestIntSuccessComposeFSM '),
    
    ('Generate SVG',
     'dotsvg TestIntSuccessComposeFSM '),

    ('Compose model with forbidden trace',
     'pma.py -o TestIntWrongComposeFSM TestIntWrong WebModel'),

    ('Generate dot',
     'pmg.py TestIntWrongComposeFSM'),
    
    ('Generate SVG',
     'dotsvg TestIntWrongComposeFSM'),
]
