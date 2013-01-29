"""
msocket tests with stepper_o and observables
"""

# Subsequent runs use different port numbers
# so output is not completely reproducible

cases = [
    ('Just the model, no scenarios or configurations',
     'pmt.py -n 10 -c 6 -t 5 msocket observables -i stepper_o'),
     
    ('Synchronous: no blocking, next action after send_all is send_return, etc.',
     'pmt.py -n 10 -c 6 -t 5 msocket observables synchronous -i stepper_o'),

    ('Synchronous and deterministic: entire message is always sent, then received',
     'pmt.py -n 10 -c 6 -t 5 msocket observables deterministic synchronous -i stepper_o'),
    ]
