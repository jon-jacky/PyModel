"""
test_stepper_d - msocket tests with deterministic stepper_d
"""

cases = [
    ('Just the model, no scenarios or configurations',
     'pmt -n 10 -c 6 msocket -i stepper_d'),
     
    ('Synchronous: no blocking, next action after send_all is send_return, etc.',
     'pmt -n 10 -c 6 msocket synchronous -i stepper_d'),

    ('Synchronous and deterministic: entire message is always sent, then received',
     'pmt -n 10 -c 6 msocket deterministic synchronous -i stepper_d'),
    ]
