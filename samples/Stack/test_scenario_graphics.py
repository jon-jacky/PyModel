cases = [
    ('Scenarios module with three runs, by itself',
     'pma Scenarios'),
    ('Generate Dot', 'pmg ScenariosFSM'),
    ('Generate SVG', 'dotsvg ScenariosFSM'),

    ('Scenarios module, compose with Stack model, last three runs not allowed',
     'pma -o ValidateScenarios Scenarios Stack'),
    ('Generate Dot', 'pmg ValidateScenarios'),
    ('Generate SVG', 'dotsvg ValidateScenarios'),

    ('Scenarios, compose with Stack, Push is observable',
     'pma -o ValidateObservables Scenarios Stack Observables'),
    ('Generate Dot', 'pmg ValidateObservables'),
    ('Generate SVG', 'dotsvg ValidateObservables'),

    ('Scenarios, compose with Stack, Push and Pop are observable',
     'pma -o ValidateAllObservables Scenarios Stack AllObservables'),
    ('Generate Dot', 'pmg ValidateAllObservables'),
    ('Generate SVG', 'dotsvg ValidateAllObservables')
    ]
