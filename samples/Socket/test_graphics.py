"""
Socket model graphics tests
"""

cases = [
    ('Generate an FSM with 100 transitions from the model with default domains',
     'pma.py Socket'),

    ('Generate graphics',
     'pmg.py SocketFSM'),

    ('Generate an SVG file you can display in a browser',
     'dotsvg SocketFSM'),

    ('Generate an FSM with from the model with more restricted domains',
     'pma.py -o SocketFSMA Socket SocketSendA'),

    ('Generate graphics',
     'pmg.py SocketFSMA'),

    ('Generate an SVG file you can display in a browser',
     'dotsvg SocketFSMA'),

    ('Generate graphics from non-blocking scenario',
     'pmg.py NoBlockScenario'),

    ('Generate an SVG file',
     'dotsvg NoBlockScenario'),

    ('Compose model with no-blocking scenario',
     'pma.py -o NoBlockComposeFSM Socket NoBlockScenario'),

    ('Generate graphics',
     'pmg.py NoBlockComposeFSM'),

    ('Generate an SVG file',
     'dotsvg NoBlockComposeFSM'),

    ('Compose model with no-blocking scenario, smaller domain',
     'pma.py -o NoBlockComposeFSMA Socket NoBlockScenario SocketSendA'),

    ('Generate graphics',
     'pmg.py NoBlockComposeFSMA'),

    ('Generate an SVG file',
     'dotsvg NoBlockComposeFSMA'),

    ('Non-blocking, also rebind enabling conditions so entire message sent, received',
     'pma.py SendAll Socket NoBlockScenario'),

    ('Generate graphics',
     'pmg.py SendAllFSM'),

    ('Generate an SVG file',
     'dotsvg SendAllFSM')
]
