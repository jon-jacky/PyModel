"""
observation queue used by steppers that return observable actions.
"""

import collections
import threading

# stepper sets asynch = True to make pmt wait for asynch observable actions
asynch = False  # default: pmt doesn't wait for observable actions

queue = collections.deque() # initially empty

# initially clear, stepper sets when new item in queue, pmt clears when remove
event = threading.Event() 
