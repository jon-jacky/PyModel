"""
Test WebModel graphics
"""

cases = [
    # limit exploration by -m 

    ('Explore WebModel, limit exploration by -m',
     'pma WebModel -m 50'),

    ('Generate dot graphics commands',
     'pmg WebModelFSM'),
    
    ('Generate SVG file',
     'dotsvg WebModelFSM'),
    
    # limit exploration by domain

    ('Explore Webmodel, limit exploration by domain OneUserDomain',
     'pma OneUserDomain WebModel'),

    ('Generate dot graphics commands',
     'pmg OneUserDomainFSM'),
    
    ('Generate SVG file',
     'dotsvg OneUserDomainFSM'),

    # limit exploration by scenario FSM

    # FSM that allows interleaving with UpdateInt, ReadInt actions
    ('Generate dot from scenario FSM',
     'pmg OneUserScenario'),
    
    ('Generate SVG',
     'dotsvg OneUserScenario'),
    
    # Composition with FSM
    ('Explore WebModel, limit exploration by scenario FSM OnUserScenario',
     'pma OneUserScenario WebModel'),

    ('Generate dot',
     'pmg OneUserScenarioFSM'),
    
    ('Generate SVG',
     'dotsvg OneUserScenarioFSM'),

    # limit exploration by state filter

    ('Explore WebModel, limit exploration by state filter OneUserFilter',
     'pma OneUserFilter WebModel'),

    ('Generate dot',
     'pmg OneUserFilterFSM'),
    
    ('Generate SVG',
     'dotsvg OneUserFilterFSM'),

    # Again limit exploration by scenario FSM

    # FSM that suppresses interleaving with UpdateInt, ReadInt actions
    ('Generate dot from scenario FSM',
     'pmg OneUserNoIntScenario'),
    
    ('Generate SVG',
     'dotsvg OneUserNoIntScenario'),
    
    # Composition with FSM
    ('Explore WebModel, limit exploration by scenario FSM OnUserScenario',
     'pma OneUserNoIntScenario WebModel'),

    ('Generate dot',
     'pmg OneUserNoIntScenarioFSM'),
    
    ('Generate SVG',
     'dotsvg OneUserNoIntScenarioFSM'),
]
