"""
Controllable/observable, synchronous, non-deterministic stepper for Socket
(see Stepper.py header for explanations.)

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
recv_call/return here to Stepper.py).

This stepper is still synchronous - each _call action must be
immediately followed by its _return action, otherwise the call to
test_action will block.

Example: pmt.py -i stepper_o Socket SendAll NoBlockScenario
"""

import socket
from observation_queue import observation_queue

# Default configuration, may rebind below

port = 8080
line_length = 80  # length limit for received messages

# Server's listener socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rcvbuf = listener.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)

# Release listener socket immediately when program exits, 
# avoid socket.error: [Errno 48] Address already in use
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Wait for client to connect
listener.bind(('localhost', port))
listener.listen(1) 
print '\nServer listening on localhost port %s with RCVBUF %s' % (port, rcvbuf)

# Client socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sndbuf = client.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
print 'Client creates socket with SNDBUF %s' % (sndbuf)

# Client connect
client.connect(('localhost', port))
print 'Client connecting to localhost port %s' % port

# Server accepts connection
server, addr = listener.accept()
print 'Server accepted from ', addr

# Now can client can repeat client.send(data) until EOF,
# then should client.close
# Now server can read by repeating data=server.recv(n) until EOF
# Then should server.close()

# Test the connection
client.send('Hello world!')
data = server.recv(line_length)
print 'Try a test message, server got "%s"\n' % data

def test_action(aname, args, modelResult):
  """
  In the test_action branch for each controllable action, the code for
  the _call action waits (synchronously) for the implemenation to 
  return, then uses the observed return value to construct and return 
  the _return action (which may include nondeterministic return values).

  For now send_ always invokes client.send and recv_ always invokes server.recv
  """

  global msg, n, bufsize # state needed to remember _call args for _return

  if aname == 'send_call':
    (msg,) = args # extract msg from args tuple, like msg = args[0]
    nchars = client.send(msg)
    # append result to observation queue
    observation_queue.append(('send_return', (nchars,)))
    return None # pmt will check observation_queue

  elif aname == 'send_close':
    client.close()

  # send_exception shouldn't appear in synchronous scenarios
  
  elif aname == 'recv_call':
    (bufsize,) = args
    data = server.recv(bufsize)
    observation_queue.append(('recv_return', (data,)))
    return None

  elif aname == 'recv_close':
    server.close()

  else:
    raise NotImplementedError, 'action not supported by stepper: %s' % aname


def reset():
  global client, server, addr
  # Assume both ends, client and server, are already closed.
  # Model assumes connection already established in initial state.
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect(('localhost', port))
  server, addr = listener.accept()
  observation_queue.clear()
  print 'Server accepted from ', addr


