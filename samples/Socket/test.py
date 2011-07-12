"""
Socket model tests
"""

cases = [
    ('Model only, shows interleaving between _call and _return',
     'pmt.py -s 8 -n 20 Socket'),
    
    ('Compose model with non-blocking scenario that ensures _call then _return',
     'pmt.py -s 11 -n 20 Socket NoBlockScenario'),

    ('Compose model with scenario, config to make behavior synchronous, deterministic',
     'pmt.py -s 2 -r 6 SendAll Socket NoBlockScenario')
    ]

