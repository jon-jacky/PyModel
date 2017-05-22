"""
stepper_d - ontrollable, synchronous, deterministic stepper for msocket

Controllable means all actions are functions that are called by the
stepper.  No actions are events that are detected by the stepper.
We make the stepper all-controllable by including *both* sender and
receiver in the stepper, both running in one thread on localhost.

Synchronous means no blocking: the next action after send_call is
always send_return, etc.  To make model behavior synchronous, compose
msocket with the synchronous scenario machine.  The implementation must
obey because in this stepper all actions are controllable.

Deterministic means the entire message is always sent, and the entire
message always received.  To make model behavior deterministic, use
the deterministic configuration module.  BUT the implementation cannot
be made to obey.  Implementation behavior that differs from the model
will be reported as test failures.  Although the model allows
nondeterministic behavior, this stepper does not.  Implementation
behavior is likely to be deterministic if messages are small enough.

Example: pmt -n 10 -c 6 -i stepper_d msocket synchronous nondeterministic
"""

# We must import stepper_util.sender, receiver this way, 
#  or they don't work in runs after the first one, after executing reset
import stepper_util as connection

# But we can import these items in this way, they do work after reset -- why?
from stepper_util import reset, msg, n, bufsize, line_length

def test_action(aname, args, model_result):
  """
  To indicate success, return None (no return statement).
  To indicate failure, return string that explains failure.
  Test runner also treats unhandled exceptions as failures.

  This is the synchronous stepper so send_call is always immediately
  followed by send_return, etc.  Therefore all the _call branches are
  empty, do all the work in the _return branches.

  send_return always invokes sender.send and recv_return always
  invokes receiver.recv

  model_result must appear in arg list but it is not used here, 
  instead model results are passed in _return args
  """

  global msg, n, bufsize # state needed to remember _call args for _return

  if aname == 'send_call':
    (msg,) = args

  elif aname == 'send_return':
    (n,) = args 
    nchars = connection.sender.send(msg)
    if n != nchars:
      return 'send returned %s, expected %s ' % (nchars, n)

  elif aname == 'recv_call':
    (bufsize,) = args

  elif aname == 'recv_return':
    (msg,) = args 
    data = connection.receiver.recv(bufsize)
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
    raise NotImplementedError('action not supported by stepper: %s' % aname)
