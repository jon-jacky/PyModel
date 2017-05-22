"""
stepper_o - synchronous but non-deterministic stepper for msocket

Controllable/observable, synchronous, non-deterministic stepper for socket
(see stepper_d.py header and allabout.txt for explanations).

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

This stepper is still synchronous - each _call action must be
immediately followed by its _return action, otherwise the call to
test_action will block.

Example: pmt -n 10 -c 6 msocket observables synchronous -i stepper_o
"""

# We must import stepper_util.sender, receiver this way, 
#  or they don't work in runs after the first one, after executing reset
import stepper_util as connection

# But we can import these items in this way, they do work after reset -- why?
from stepper_util import reset

import observation_queue as observation

def test_action(aname, args, modelResult):
  """
  In the test_action branch for each controllable action, the code for
  the _call action waits (synchronously) for the implemenation to 
  return, then uses the observed return value to construct and return 
  the _return action (which may include nondeterministic return values).

  For now send_ always invokes sender.send and recv_ always invokes receiver.recv
  """

  if aname == 'send_call':
    (msg,) = args # extract msg from args tuple, like msg = args[0]
    n = connection.sender.send(msg)
    observation.queue.append(('send_return', (n,)))
    return None # pmt will check observation_queue
  
  elif aname == 'recv_call':
    (bufsize,) = args
    msg = connection.receiver.recv(bufsize)
    observation.queue.append(('recv_return', (msg,)))
    return None # pmt will check observation_queue

  else:
    raise NotImplementedError('action not supported by stepper: %s' % aname)
