"""
Test WebModel graphics
"""

cases = [
    # limit exploration by -m 

    ('Explore WebModel, limit exploration by -m',
     'pma.py WebModel -m 50'),

    ('Generate dot graphics commands',
     'pmg.py WebModelFSM'),
    
    ('Generate SVG file',
     'dotsvg WebModelFSM'),
    
    # limit exploration by domain

    ('Explore Webmodel, limit exploration by domain OneUserDomain',
     'pma.py OneUserDomain WebModel'),

    ('Generate dot graphics commands',
     'pmg.py OneUserDomainFSM'),
    
    ('Generate SVG file',
     'dotsvg OneUserDomainFSM'),

    # limit exploration by scenario FSM

    # FSM that allows interleaving with UpdateInt, ReadInt actions
    ('Generate dot from scenario FSM',
     'pmg.py OneUserScenario'),
    
    ('Generate SVG',
     'dotsvg OneUserScenario'),
    
    # Composition with FSM
    ('Explore WebModel, limit exploration by scenario FSM OnUserScenario',
     'pma.py OneUserScenario WebModel'),

    ('Generate dot',
     'pmg.py OneUserScenarioFSM'),
    
    ('Generate SVG',
     'dotsvg OneUserScenarioFSM'),

    # limit exploration by state filter

    ('Explore WebModel, limit exploration by state filter OneUserFilter',
     'pma.py OneUserFilter WebModel'),

    ('Generate dot',
     'pmg.py OneUserFilterFSM'),
    
    ('Generate SVG',
     'dotsvg OneUserFilterFSM'),

    # Again limit exploration by scenario FSM

    # FSM that suppresses interleaving with UpdateInt, ReadInt actions
    ('Generate dot from scenario FSM',
     'pmg.py OneUserNoIntScenario'),
    
    ('Generate SVG',
     'dotsvg OneUserNoIntScenario'),
    
    # Composition with FSM
    ('Explore WebModel, limit exploration by scenario FSM OnUserScenario',
     'pma.py OneUserNoIntScenario WebModel'),

    ('Generate dot',
     'pmg.py OneUserNoIntScenarioFSM'),
    
    ('Generate SVG',
     'dotsvg OneUserNoIntScenarioFSM'),
]
