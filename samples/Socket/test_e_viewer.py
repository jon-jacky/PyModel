"""
Test -e option in FSMs, using pmv
"""

cases = [
    ('No -e option',
     'pmv NoBlockScenario'),

    ('Now same command with -e send_close -e recv_close',
    'pmv -e send_close -e recv_close NoBlockScenario -o NoBlockScenario_e'),
]

