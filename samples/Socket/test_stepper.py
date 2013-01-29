"""
msocket tests with stepper
"""

# Subsequent runs use different port numbers
# so output is not completely reproducible

cases = [
    ('Just the model, no scenarios or configurations',
     'pmt.py -n 10 -c 6 msocket -i stepper'),
     
    ('Synchronous: no blocking, next action after send_all is send_return, etc.',
     'pmt.py -n 10 -c 6 msocket synchronous -i stepper'),

    ('Synchronous and deterministic: entire message is always sent, then received',
     'pmt.py -n 10 -c 6 msocket deterministic synchronous -i stepper'),
    ]
