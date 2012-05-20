"""
Socket model tests that demonstrate blocking
Blocking occurs whenever _call is not immediately followed by its _return
"""

cases = [
    ('Test suite only, use -q to suppress echo of very large messages',
     'pmt.py -q block send_aa'),

    ('Test suite with model',
     'pmt.py -q block send_aa Socket'),

    ('Test suite with model and stepper_o, should block then time out',
     'pmt.py block send_aa observables -i stepper_o -q -t 5')
]
