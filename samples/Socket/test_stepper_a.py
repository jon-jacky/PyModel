"""
test_stepper_a - msocket tests with asynchronous stepper_a using threads
"""

cases = [
    ('Just the model, no scenarios or configurations',
     'pmt -n 10 -c 6 -t 5 msocket observables -i stepper_a'),
    ]
