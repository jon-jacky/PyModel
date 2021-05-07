"""
Simple Stepper to experiment with timeouts in pmt
"""

import time

def TestAction(aname, args, modelResult):
    if aname == 'sleep':
        (seconds,) = args
        time.sleep(seconds)
    else:
        raise NotImplementedError('action not supported by stepper: %s' % aname)

def Reset():
    pass
