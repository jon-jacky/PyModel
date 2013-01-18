"""
Socket model - view same compositions and configurations as in test.py
"""

cases = [
    ('Model only, shows interleaving between _call and _return',
     'pmv socket'),
    
    ('Compose model with synchronous scenario that ensures _call then _return',
     'pmv synchronous socket'),

    ('Add state-dependent domains to make behavior deterministic',
     'pmv deterministic synchronous socket')
    ]
