"""
Controllable, synchronous, deterministic stepper for msocket

Controllable means all actions are functions that are called by the
stepper.  No actions are events that are detected by the stepper.
Make the stepper all-controllable by including *both* server and
client in the stepper, both running in one thread on localhost.

Synchronous means no blocking: next action after send_call is
send_return, etc.  To make model behavior synchronous, compose msocket
with the synchronous scenario machine.  Implementation must obey
because in this stepper all actions are controllable.

Deterministic means entire message is always sent, entire msg always received.
To make model behavior deterministic, use the deterministic config. module.
The implementation cannot be made to obey.  Nondeterministic
implementation behavior will be reported as test failures. Implementation
behavior is likely to be deterministic if messages are small enough.

Example: pmt.py -n 10 -c 6 -i stepper msocket synchronous nondeterministic
"""

import socket  # Python standard library socket module, OR a simulator

# Default configuration, may rebind below
port = 8080
line_length = 80  # length limit for received messages

# Initial setup, runs once when test runner pmt imports stepper 

# Server's listener socket
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get and recv buffer size to print below, just FYI
rcvbuf = listener.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)

# Ensure we release listener socket immediately when program exits, 
#  to avoid socket.error: [Errno 48] Address already in use
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Listen, prepare for clients to connect
listener.bind(('localhost', port))
listener.listen(1) 
print '\nServer listens on localhost port %s with RCVBUF size %s' % (port, rcvbuf)

# Define function for client connect - also used in stepper reset()
def new_connection():
  global client, server, addr, msg, n, bufsize
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # get and print send buffer size, just FYI
  sndbuf = client.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
  print 'Client creates socket with SNDBUF size %s' % (sndbuf)
  client.connect(('localhost', port))
  print 'Client connects to localhost port %s' % port
  server, addr = listener.accept()
  print 'Server accepts connection from ', addr
  # State needed to remember _call args for __return
  msg = ''
  n = 0
  bufsize = 0

# Now call that function to connect the first time
new_connection()

def close_connection():
  global client, server
  client.close()
  server.close()

def reset():
  close_connection()
  new_connection()

def test_action(aname, args, modelResult):
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

  elif aname == 'recv_call':
    (bufsize,) = args

  elif aname == 'recv_return':
    (msg,) = args 
    data = server.recv(bufsize)
    if data != msg: # now msg is like old modelresult
      # wrapped failMessage should fit on two 80 char lines, 
      # failMessage prefix from pmt is 20 char, fixed text here is > 32 char
      maxlen = 40 # max number of chars from msg to print in failMessage
      nd = len(data)
      nm = len(msg)
      sdata =  data if nd <= maxlen \
          else data[:maxlen/2] + '...' + data[-maxlen/2:]
      smodel =  msg if nm <= maxlen \
          else msg[:maxlen/2] + '...' + msg[-maxlen/2:]
      return 'recv returned %s (%s), expected %s (%s)' % (sdata, nd, smodel, nm)

  else:
    raise NotImplementedError, 'action not supported by stepper: %s' % aname


