"""
Marquee graphics and domains tests

Generate the same *FSM.py and *.svg as test_graphics in this sample,
but this script is shorter because it uses pmv instead of pma + pmg + dot
"""

cases = [
    ('Explore Marquee with default domains',
     'pmv Marquee'),

    ('Explore Marquee with modified domains, allow Load at any time',
     'pmv DisplayFive Marquee'),

    ('Same as above, but reverse argument order of module and configuration',
     'pmv -o DisplayFiveFSM1 Marquee DisplayFive'),

    ('Generate graphics commands from scenario FSM used for composition',
     'pmv LoadFirst'),

    ('Explore with modified domains, with scenario that allows initial Load only',
     'pmv -o PeriodFiveFSM Marquee DisplayFive LoadFirst'),

    ('Ditto, change argument order',
     'pmv -o PeriodFiveFSM1 LoadFirst Marquee DisplayFive'),

    ('Change argument order again',
     'pmv -o PeriodFiveFSM2 DisplayFive Marquee LoadFirst'),

]
