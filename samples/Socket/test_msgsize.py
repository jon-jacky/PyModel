"""
test_msgsize - exercise deterministic msocket stepper_d with large messages
"""

cases = [
    ("""Exercise the deterministic socket stepper with some very large messages
to reveal its limitations: this stepper fails some behaviors allowed by the model.
 The first two test runs are supposed to fail. ...""",
     'pmt msgsizes -i stepper_d all_observables -q -t 5')

]
