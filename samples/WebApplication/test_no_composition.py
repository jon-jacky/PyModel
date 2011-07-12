"""
Test three model program classes with return values but without composition
"""

cases = [    
    # TestSuite
    ('TestSuite: generate FSM from scenario',
     'pma.py TestIntSuccess'),

    ('Generate dot',
     'pmg.py TestIntSuccessFSM'),
    
    ('Generate SVG',
     'dotsvg TestIntSuccessFSM'),

    # FSM
    ('FSM: Generate FSM from scenario FSM',
     'pma.py OneUserScenario'),

    ('Generate dot',
     'pmg.py OneUserScenarioFSM'),

    ('Generate SVG',
     'dotsvg OneUserScenarioFSM'),

    # ModelProgram
    ('Model Program: Generate FSM by exploring WebModel',
     'pma.py WebModel -m 20'),

    ('Generate dot graphics commands',
     'pmg.py WebModelFSM'),
    
    ('Generate SVG file',
     'dotsvg WebModelFSM'),
]
