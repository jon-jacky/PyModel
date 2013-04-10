cases = [
    ('ScenarioLogin module by itself',
     'pmt ScenarioLogin'),

    ('ScenarioLogin composed with WebModel, no -n necessary',
     'pmt -s 1 ScenarioLogin WebModel'),

    ('OneUserScenario, by itself, -n is necessary but not -s',
     'pmt -n 6 OneUserScenario'),

    ('OneUserScenario composed with WebModel with -n and -s',
     'pmt -n 20 -s 2 OneUserScenario WebModel')
    ]
