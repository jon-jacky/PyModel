"""
Controllable, synchronous, deterministic stepper for Socket

Controllable means all actions are functions that are called by the
stepper.  No actions are events that are detected by the stepper.
Make the stepper all-controllable by including *both* server and
client in the stepper, both running in one thread on localhost.

Synchronous means no blocking: next action after send_call is send_return, etc.
To make model behavior synchronous, compose Socket with NoBlockScenario.
Implementation must obey because in this stepper all actions are controllable.

Deterministic means entire message is always sent, entire msg always received.
To make model behavior deterministic, use the SendAll config. module.
The implementation cannot be made to obey.  Nondeterministic
implementation behavior will be reported as test failures. Implementation
behavior is likely to be deterministic if messages are small enough.

Example: pmt.py -i Stepper Socket SendAll NoBlockScenario
"""

import socket

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

# State needed to remember _call args for __return
msg = ''
n = 0
bufsize = 0

def testaction(aname, args, modelResult):
  """
  To indicate success, return None (no return statement).
  To indicate failure, return string that explains failure.
  Test runner also treats unhandled exceptions as failures.

  This is the synchronous stepper so send_call is always immediately
  followed by send_return, etc.  Therefore all the _call branches are
  empty, do all the work in the _return branches.

  For now send_ always invokes client.send and recv_ always invokes server.recv
  """

  global msg, n, bufsize # state needed to remember _call args for _return

  if aname == 'send_call':
    (msg,) = args

  elif aname == 'send_return':
    (n,) = args 
    nchars = client.send(msg)
    if n != nchars:
      return 'send returned %s, expected %s ' % (nchars, n)

  elif aname == 'send_close':
    client.close()

  # send_exception shouldn't appear in synchronous scenarios
  
  elif aname == 'recv_call':
    (bufsize,) = args

  elif aname == 'recv_return':
    (n,) = args
    data = server.recv(bufsize)
    if data != modelResult:
      # wrapped failMessage should fit on two 80 char lines, 
      # failMessage prefix from pmt is 20 char, fixed text here is > 32 char
      maxlen = 40 # max number of chars from msg to print in failMessage
      nd = len(data)
      nm = len(modelResult)
      sdata =  data if nd <= maxlen \
          else data[:maxlen/2] + '...' + data[-maxlen/2:]
      smodel =  modelResult if nm <= maxlen \
          else modelResult[:maxlen/2] + '...' + modelResult[-maxlen/2:]
      return 'recv returned %s (%s), expected %s (%s)' % (sdata, nd, smodel, nm)

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
  print 'Server accepted from ', addr


