"""
Socket model tests
"""

cases = [
    ('Model only, shows interleaving between _call and _return',
     'pmt -n 10 -c 6 socket'),
    
    ('Compose model with synchronous scenario that ensures _call then _return',
     'pmt -n 10 -c 6 synchronous socket'),

    ('Add state-dependent domains to make behavior deterministic',
     'pmt -n 10 -c 6 deterministic synchronous socket')
    ]

