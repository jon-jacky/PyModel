"""
msocket tests with stepper
"""

# Subsequent runs use different port numbers
# so output is not completely reproducible

cases = [
    ('Synchronous: no blocking, next action after send_all is send_return, etc.',
     'pmt.py -n 10 -c 6 -r 3  msocket synchronous -i stepper'),

    ('Synchronous and deterministic: entire message is always sent, then received',
     'pmt.py -n 10 -c 6 -r 3 msocket deterministic synchronous -i stepper'),
    ]
