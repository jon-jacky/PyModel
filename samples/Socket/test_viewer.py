"""
test_viewer - msocket model, view same compositions and configurations as in test.py
"""

cases = [
    ('Model only, shows interleaving between _call and _return',
     'pmv msocket'),

    ('Synchronous scenario, graph of the FSM',
     'pmv -o synchronous_graph synchronous'),

    ('Compose model with synchronous scenario that ensures _call then _return',
     'pmv synchronous msocket'),

    ('Add state-dependent domains to make behavior deterministic',
     'pmv deterministic synchronous msocket')
    ]
