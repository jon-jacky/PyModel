"""
test.py - msocket model tests
"""

cases = [
    ('Model only, shows interleaving between _call and _return',
     'pmt -n 10 -c 6 msocket'),
    
    ('Compose model with synchronous scenario that ensures _call then _return',
     'pmt -n 10 -c 6 synchronous msocket'),

    ('Add state-dependent domains to make behavior deterministic',
     'pmt -n 10 -c 6 deterministic synchronous msocket')
    ]

