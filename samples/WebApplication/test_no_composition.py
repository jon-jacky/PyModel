"""
Test three model program classes with return values but without composition
"""

cases = [    
    # TestSuite
    ('TestSuite: generate FSM from scenario',
     'pma TestIntSuccess'),

    ('Generate dot',
     'pmg TestIntSuccessFSM'),
    
    ('Generate SVG',
     'dotsvg TestIntSuccessFSM'),

    # FSM
    ('FSM: Generate FSM from scenario FSM',
     'pma OneUserScenario'),

    ('Generate dot',
     'pmg OneUserScenarioFSM'),

    ('Generate SVG',
     'dotsvg OneUserScenarioFSM'),

    # ModelProgram
    ('Model Program: Generate FSM by exploring WebModel',
     'pma WebModel -m 20'),

    ('Generate dot graphics commands',
     'pmg WebModelFSM'),
    
    ('Generate SVG file',
     'dotsvg WebModelFSM'),
]
