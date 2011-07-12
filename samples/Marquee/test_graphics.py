"""
Marquee graphics and domains tests
"""

cases = [
    ('Explore Marquee with default domains',
     'pma.py Marquee'),

    ('Generate graphics commands',
     'pmg.py MarqueeFSM'),

    ('Generate graphics file',
     'dotsvg MarqueeFSM'),

    ('Explore Marquee with modified domains, allow Load at any time',
     'pma.py DisplayFive Marquee'),

    ('Generate graphics commands',
     'pmg.py DisplayFiveFSM'),

    ('Generate graphics file',
     'dotsvg DisplayFiveFSM'),

    ('Same as above, but reverse argument order of module and configuration',
     'pma.py -o DisplayFiveFSM1 Marquee DisplayFive'),

    ('Generate graphics commands',
     'pmg.py DisplayFiveFSM1'),

    ('Generate graphics file',
     'dotsvg DisplayFiveFSM1'),

    ('Generate graphics commands from scenario FSM used for composition',
     'pmg.py LoadFirst'),

    ('Generate graphics file',
     'dotsvg LoadFirst'),

    ('Explore with modified domains, with scenario that allows initial Load only',
     'pma.py -o PeriodFiveFSM Marquee DisplayFive LoadFirst'),

    ('Generate graphics commands',
     'pmg.py PeriodFiveFSM'),

    ('Generate graphics file',
     'dotsvg PeriodFiveFSM'),

    ('Ditto, change argument order',
     'pma.py -o PeriodFiveFSM1 LoadFirst Marquee DisplayFive'),

    ('Generate graphics commands',
     'pmg.py PeriodFiveFSM1'),

    ('Generate graphics file',
     'dotsvg PeriodFiveFSM1'),

    ('Change argument order again',
     'pma.py -o PeriodFiveFSM2 DisplayFive Marquee LoadFirst'),

    ('Generate graphics commands',
     'pmg.py PeriodFiveFSM2'),

    ('Generate graphics file',
     'dotsvg PeriodFiveFSM2'),
]
