"""
Socket model viewer  tests
"""

cases = [
    ('No -e options',
     'pmv.py -o send_aa_small_no_e_FSM send_aa_small Socket len_buffers_two'),

    ('Two -e options in a single command',
     'pmv.py send_aa_small Socket len_buffers_two -e send_close -e recv_close'),

    ('Same graph, this time generate PDF',
     'pmv.py -T pdf send_aa_small Socket len_buffers_two -e send_close -e recv_close')
]
