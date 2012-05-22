"""
observation queue used by steppers that return observable actions.
"""

import collections

observation_queue = collections.deque() # initially empty
