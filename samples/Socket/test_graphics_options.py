"""
Socket model graphics tests, test pmg options
"""

cases = [


    ('Non-blocking, also rebind enabling conditions so entire message sent, received',
     'pma.py SendAll Socket NoBlockScenario'),

    ('Generate graphics with default action labels',
     'pmg.py SendAllFSM'),
    ('Generate an SVG file',
     'dotsvg SendAllFSM'),

    ('Generate graphics with action name labels',
     'pmg.py -o SendAllNameLabelFSM -l name SendAllFSM'),
    ('Generate an SVG file',
     'dotsvg SendAllNameLabelFSM'),

    ('Generate graphics with no action labels',
     'pmg.py -o SendAllNoLabelFSM -l none SendAllFSM'),
    ('Generate an SVG file',
     'dotsvg SendAllNoLabelFSM'),

    ('Generate graphics with no action labels and no tooltips',
     'pmg.py -o SendAllNoTooltipFSM -l none -xy SendAllFSM'),
    ('Generate an SVG file',
     'dotsvg SendAllNoTooltipFSM'),
]
