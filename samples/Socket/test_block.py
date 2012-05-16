"""
Socket model tests that demonstrate blocking
Blocking occurs whenever _call is not immediately followed by its _return
"""

cases = [
    ('Test suite only, use -q to suppress echo of very large messages',
     'pmt.py -q block send_aa'),

    ('Test suite with model',
     'pmt.py -q block send_aa Socket'),
]
