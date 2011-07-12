cases = [
    ('ScenarioLogin module by itself',
     'pmt.py ScenarioLogin'),

    ('ScenarioLogin composed with WebModel, no -n necessary',
     'pmt.py -s 1 ScenarioLogin WebModel'),

    ('OneUserScenario, by itself, -n is necessary but not -s',
     'pmt.py -n 6 OneUserScenario'),

    ('OneUserScenario composed with WebModel with -n and -s',
     'pmt.py -n 20 -s 2 OneUserScenario WebModel')
    ]
