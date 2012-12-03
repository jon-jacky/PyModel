"""
Test -e option in FSMs, using pmt
"""

cases = [
    ('No -e options: pmt -n 10 NoBlockScenario',
     'pmt -n 10 NoBlockScenario'),

    ('Now same command with -e send_close -e recv_close',
     'pmt -e send_close -e recv_close -n 10 NoBlockScenario'),
]

