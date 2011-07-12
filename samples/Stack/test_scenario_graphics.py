cases = [
    ('Scenarios module with three runs, by itself',
     'pma.py Scenarios'),
    ('Generate Dot', 'pmg.py ScenariosFSM'),
    ('Generate SVG', 'dotsvg ScenariosFSM'),

    ('Scenarios module, compose with Stack model, last three runs not allowed',
     'pma.py -o ValidateScenarios Scenarios Stack'),
    ('Generate Dot', 'pmg.py ValidateScenarios'),
    ('Generate SVG', 'dotsvg ValidateScenarios'),

    ('Scenarios, compose with Stack, Push is observable',
     'pma.py -o ValidateObservables Scenarios Stack Observables'),
    ('Generate Dot', 'pmg.py ValidateObservables'),
    ('Generate SVG', 'dotsvg ValidateObservables'),

    ('Scenarios, compose with Stack, Push and Pop are observable',
     'pma.py -o ValidateAllObservables Scenarios Stack AllObservables'),
    ('Generate Dot', 'pmg.py ValidateAllObservables'),
    ('Generate SVG', 'dotsvg ValidateAllObservables')
    ]
