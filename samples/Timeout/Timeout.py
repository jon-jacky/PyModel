"""
Simple test suite to experiment with timeouts in pmt
"""

def sleep(seconds): pass

actions = (sleep,)

testSuite = [
    [
        (sleep, (2,), None),
        (sleep, (5,), None),
        (sleep, (10,), None),
        (sleep, (20,), None)
     ]
]
