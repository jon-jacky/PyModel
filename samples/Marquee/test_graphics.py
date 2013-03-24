"""
Marquee graphics and domains tests
"""

cases = [
    ('Explore Marquee with default domains',
     'pma Marquee'),

    ('Generate graphics commands',
     'pmg MarqueeFSM'),

    ('Generate graphics file',
     'dotsvg MarqueeFSM'),

    ('Explore Marquee with modified domains, allow Load at any time',
     'pma DisplayFive Marquee'),

    ('Generate graphics commands',
     'pmg DisplayFiveFSM'),

    ('Generate graphics file',
     'dotsvg DisplayFiveFSM'),

    ('Same as above, but reverse argument order of module and configuration',
     'pma -o DisplayFiveFSM1 Marquee DisplayFive'),

    ('Generate graphics commands',
     'pmg DisplayFiveFSM1'),

    ('Generate graphics file',
     'dotsvg DisplayFiveFSM1'),

    ('Generate graphics commands from scenario FSM used for composition',
     'pmg LoadFirst'),

    ('Generate graphics file',
     'dotsvg LoadFirst'),

    ('Explore with modified domains, with scenario that allows initial Load only',
     'pma -o PeriodFiveFSM Marquee DisplayFive LoadFirst'),

    ('Generate graphics commands',
     'pmg PeriodFiveFSM'),

    ('Generate graphics file',
     'dotsvg PeriodFiveFSM'),

    ('Ditto, change argument order',
     'pma -o PeriodFiveFSM1 LoadFirst Marquee DisplayFive'),

    ('Generate graphics commands',
     'pmg PeriodFiveFSM1'),

    ('Generate graphics file',
     'dotsvg PeriodFiveFSM1'),

    ('Change argument order again',
     'pma -o PeriodFiveFSM2 DisplayFive Marquee LoadFirst'),

    ('Generate graphics commands',
     'pmg PeriodFiveFSM2'),

    ('Generate graphics file',
     'dotsvg PeriodFiveFSM2'),
]
