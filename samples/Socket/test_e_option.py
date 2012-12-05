"""
Test -e option in FSMs, using pmt
"""

cases = [
    ('No -e options: pmt -n 10 NoBlockScenario',
     'pmt -n 10 NoBlockScenario'),

    ('Same FSM with -e send_close -e recv_close',
     'pmt -e send_close -e recv_close -n 10 NoBlockScenario'),

    ('Same FSM with -e send_close -e recv_close, also -e recv_call',
     'pmt -e send_close -e recv_close -e recv_call -n 10 NoBlockScenario'),

    ('Same FSM with -a send_close -a recv_close',
     'pmt -a send_close -a recv_close -n 10 NoBlockScenario'),
]

