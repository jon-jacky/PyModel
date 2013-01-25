"""
Analyze msgsizes test suite
"""

cases = [
    ('Compose Socket model with msgsizes test suite',
     'pma.py -o msgsizesFSM msgsizes msocket all_observables'),

    ('Generate graphics, suppress tooltips because messages are too big',
     'pmg.py -l name -xy msgsizesFSM'), # -xy suppresses tooltips

    ('Generate an SVG file you can display in a browser',
     'dotsvg msgsizesFSM'),
]
