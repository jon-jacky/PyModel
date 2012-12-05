"""
Test -e and -a options in FSM, using pmv
"""

cases = [
    ('No -e options: pmv  NoBlockScenario',
     'pmv  NoBlockScenario'),

    ('Same FSM with -e send_close -e recv_close',
     'pmv -e send_close -e recv_close  NoBlockScenario -o NoBlockScenario_e'),

    ('Same FSM with -e send_close -e recv_close, also -e recv_call',
     'pmv -e send_close -e recv_close -e recv_call NoBlockScenario -o NoBlockScenario_e_e'),

    ('Same FSM with -a send_close -a recv_close',
     'pmv -a send_close -a recv_close  NoBlockScenario -o NoBlockScenario_a'),
]
