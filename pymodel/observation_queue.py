"""
observation queue used by steppers that return observable actions.

Put this in its own module so it can be imported by pmt 
and can also be optionally imported by steppers.
"""

import collections
import threading

# stepper sets asynch = True to make pmt wait for asynch observable actions
asynch = False  # default: pmt doesn't wait for observable actions

queue = collections.deque() # initially empty
