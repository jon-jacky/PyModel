"""
stepper_a - asynchronous stepper using threads.

Controllable/observable, asynchronous, non-deterministic stepper for Socket
(see stepper.py header and README.txt for explanations).

In this stepper the _return actions are observable, not controllable.
Therefore this stepper supports nondeterminism in return values.

In the test_action branch for each controllable action, the code for
the _call action constructs the observed _return action, which may
include nondeterministic return values.  It appends the _return action
to the observation queue.

Then pmt pops the _return action from the observation queue, then
calls the model to determine whether the observed _return action is
enabled.  So pmt + model determines whether the test passed or failed.
This simplifies the stepper (compare test_action branch for
recv_call/return here to stepper_d.py).

This stepper is asynchronous - a _call action need not be immediately
followed by its _return action.  Each _call is handled in its own thread,
so test_action can return even if _call blocks.

Example: pmt -i stepper_a ...
"""

import threading

# We must import stepper_util.sender, receiver this way, 
#  or they don't work in runs after the first one, after executing reset
import stepper_util as connection

# But we can import these items in this way, they do work after reset -- why?
from stepper_util import reset

import observation_queue as observation

observation.asynch = True # make pmt wait for asynch observable actions

# initially clear, stepper sets when new item in queue, pmt clears when remove
event = threading.Event() 

def test_action(aname, args, modelResult):
  """
  In the test_action branch for each controllable action, the code for
  the _call action waits (synchronously) for the implemenation to 
  return, then uses the observed return value to construct and return 
  the _return action (which may include nondeterministic return values).
  """

  if aname == 'send_call':
    def wait_for_return():
        (msg,) = args # extract msg from args tuple, like msg = args[0]
        nchars = connection.sender.send(msg)
        observation.queue.append(('send_return', (nchars,)))
        event.set() # notify pmt that data has been added to queue
    t = threading.Thread(target=wait_for_return)
    t.start()
    return None # pmt will check observation_queue

  elif aname == 'recv_call':
    def wait_for_return():
        (bufsize,) = args
        data = connection.receiver.recv(bufsize)
        observation.queue.append(('recv_return', (data,)))
        event.set() # notify pmt that data has been added to queue
    t = threading.Thread(target=wait_for_return)
    t.start()
    return None # pmt will check observation_queue

  else:
    raise NotImplementedError('action not supported by stepper: %s' % aname)


def wait(timeout):
    """
    wait for event with timeout.  If event occurs, clear event

    This function must be present in any stepper that sets 
     observation.asynch = True
    
    This function is called from the test runner pmt, 
     the event is hidden in this module.
    """
    global event
    event.wait(timeout if timeout else None)
    # FIXME?  If another event occurs right now, we will clear it and miss it!
    if event.is_set(): # if wait timed out, this will be false
        event.clear() # got this event, prepare for next
