"""
Simple test suite to experiment with timeouts in pmt
"""

def sleep(seconds): pass

actions = (sleep,)

testSuite = [
    [
        (sleep, (2,)),
        (sleep, (5,)),
        (sleep, (10,))
     ]
]
