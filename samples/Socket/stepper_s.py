"""
Asynchronous stepper using select

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
recv_call/return here to stepper.py).

This stepper is asynchronous - a _call action need not be immediately
followed by its _return action.  Instead, each subsequent call to
stepper.wait calls select, which either times out or puts an item into
the observation queue.


Example: pmt -i stepper_s ...
"""

import select

# We must import stepper_util.sender, receiver this way, 
#  or they don't work in runs after the first one, after executing reset
import stepper_util as connection

# But we can import these items in this way, they do work after reset -- why?
from stepper_util import reset

import observation_queue as observation

observation.asynch = True # make pmt wait for asynch observable actions

inbuf_size = int() # set by test_action/recv_call, read by wait/select/inputready
sendbuf = str() # set by test_action/send_call, read by wait/select/outputready

def test_action(aname, args, modelResult):
  """
  In the test_action branch for each controllable action, the code for
  the _call action waits (synchronously) for the implemenation to 
  return, then uses the observed return value to construct and return 
  the _return action (which may include nondeterministic return values).

  For now send_ always invokes client.send and recv_ always invokes server.recv
  """

  if aname == 'send_call':
    global sendbuf
    (send_msg,) = args # extract msg from args tuple, like send_msg = args[0]
    sendbuf += send_msg
    call_select(0) # timeout 0, don't block
    return None # pmt will call wait(), below

  elif aname == 'recv_call':
    global inbuf_size
    (inbuf_size,) = args
    call_select(0) # timeout 0, don't block
    return None # pmt will call wait(), below

  else:
    raise NotImplementedError, 'action not supported by stepper: %s' % aname


def wait(timeout):
    """
    Timeout might be None, wait forever

    This function must be present in any stepper that sets 
     observation.asynch = True
    
    This function is called from the test runner pmt
    """
    call_select(timeout)
    

def call_select(timeout):
    """
    use select to wait for socket input/output with timeout.
    """
    global inbuf_size, sendbuf

    inputready,outputready,exceptready = select.select([ connection.receiver ],
                                                       [ connection.sender ], 
                                                       [],timeout)
    if inputready and inbuf_size:
        # print 'inputready %s, inbuf_size %s' % (inputready, inbuf_size) # DEBUG
        recv_msg = connection.receiver.recv(inbuf_size)
        observation.queue.append(('recv_return', (recv_msg,)))
        inbuf_size = 0 

    if outputready and sendbuf:
        # print 'outputready %s, sendbuf %s' % (outputready, sendbuf)
        n = connection.sender.send(sendbuf) # DEBUG
        observation.queue.append(('send_return', (n,)))
        sendbuf = sendbuf[n:] # empty if we sent it all

    # timeout - do nothing, just return
    
