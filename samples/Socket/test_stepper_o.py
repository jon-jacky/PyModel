"""
Socket tests with stepper_o with observable actions
"""

# Subsequent runs use different port numbers
# so output is not completely reproducible

cases = [
    ('Synchronous: no blocking, next action after send_all is send_return, etc.',
     'pmt.py -s 4 -r 6 Socket NoBlockScenario observables -i stepper_o'),

    ('Synchronous and deterministic: entire message is always sent, then received',
     'pmt.py -s 4 -r 6 Socket SendAll NoBlockScenario observables -i stepper_o'),
    ]
