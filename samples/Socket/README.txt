
PyModel socket sample

This sample uses network sockets to demonstrate several PyModel
techniques for modeling and testing systems that exhibit
nondeterminism and concurrency.

To understand the discussion here, you should first read these files
in the notes directory: concepts.txt, models.txt, composition.txt, and
stepper.txt.


Motivation

Socket behavior can be more complicated than expected, because data
are buffered on each end, and may be transported through the network
at an irregular rate.  A call to send a message may block until space
becomes available in the buffers, and even then may accept only part
of the message.  A call to receive may block until data arrives in the
buffers, and even then may deliver only part of the message.  Multiple
calls to send and receive may be needed to transmit an entire message.
Nondeterminism arises from the unpredictable amount of data that is
sent or received in each call.  Concurrency arises from the
simultaneous, unsynchronized sending and receiving that add and remove
data at the two ends of the connection.  For more explanation, see:

 http://docs.python.org/howto/sockets.html
 http://pyvideo.org/video/885/through-the-ether-and-back-again-what-happens-to


Contents

The sample includes these modules:

- Socket: a model program that can exhibit nondeterminism and the
  effects of concurrency.

- NoBlockScenario, SendAll, send_aa, observables, etc.: several
  scenario machines and configuration files that select particular
  behaviors of the model program.

- Stepper, stepper_o, and stepper_a: three different steppers that use
  the model program and scenarios to test actual sockets on localhost
  (via the Python standard socket library).  Also, Sender.py,
  Receiver.py, etc.: other code for exercising the socket library.

- socket_simulator and socket_simulator_a: two simulators that can
  optionally replace the Python standard socket library in the
  steppers.  These simulators can be configured to demonstrate a great
  deal of nondeterminism and concurrency, even with small messages.

- test, test_graphics, test_stepper, test_msgsize, etc.: several test
  scripts that invoke various combinations of these modules.


Model program

The model program in the Socket module models *both* ends of the
connection.  One end of the connection is always the sender and the
other end is always the receiver: all send actions occur at one end
and all recv actions occur at the other.  Messages sent at one end can
be eventually received at the other.

This model program assumes the connection is already established in
the initial state, so it does not include actions for open, bind,
listen, accept, connect.  To test a real implementation, those must
all be handled in the stepper initialization and reset (see Stepper
sections, below).  However this model program does include close
actions for each end of the connection.  After these close actions, no
more messages can be transmitted.

The model exhibits nondeterminism, like a real socket connection.  The
send operation may accept any (incomplete) segment of its message
input, and the recv operation may return any (incomplete) segment of
the accumulated message segments that have been accepted at the sender
end.  Multiple sends and receives might be needed to transmit an
entire message.

The model exhibits concurrency, like a real socket connection.  Send
and receive actions can occur simultaneously and without
synchronization at the two ends of the connection.  Each end can send
or receive while the other end is blocked.   This is achieved by modeling
both send and receive as *two* distinct actions for the call and return:
send_call and send_return, and recv_call and recv_return.  For example, 
we might see a trace with these actions:

 recv_call
 send_call
 send_return
 recv_return

At the beginning of this trace, nothing has been sent yet.  The
receiver calls recv and blocks, because there is nothing to receive -
the buffers are empty.  Then the sender sends a message and returns,
so the receiver can read the message and return.  Here the receiver is
blocked from recv_call through recv_return, but while it is blocked
the sender can still run.  PyModel can model and test this behavior.

An action modeled in this style, where the start and finish of the
operation (here, the function call and its return) are coded as two
separate actions in the model, is called a *split action*.  It is
necessary to code split actions in order to model concurrency where
some operations can proceed while others are blocked.  

Both start and finish actions in a split action require an enabling
condition (if either is omitted, that part of the action is considered
to be enabled always).  Split actions never have return values.
Instead, the return value (or values) of the modeled action are coded
as arguments of the finish action.  So where the implemention has n =
c.send(msg) and msg = s.recv(bufsize), the model has send_call(msg)
then send_return(n), and recv_call(bufsize) and recv_return(msg).

In this model, the send and receive actions are split actions, but the
close actions are not split - they are examples of *atomic actions*.


Scenarios and configurations

The Socket model program in this sample exhibits nondeterminism and
concurrency, but these are rarely seen in the common situation where a
socket transmits small messages over a fast network.  We may wish to
restrict the behavior of the model to these common behaviors (or some
other behaviors).  Restriction can be accomplished by composing the
model program with a scenario machine.  The sample includes these
scenario machines and configuration modules:

- NoBlockScenario is an FSM where send_call is always immediately
  followed by send_return, and recv_call is always immediately
  followed by recv_return.  Composing the model program with this
  scenario machine has the effect of merging the two parts of each
  split action into a single atomic (indivisible) action.  Once
  called, each send or recv operation returns before another action
  can begin, so no interleaving is possible.  

  NoBlockScenario is demonstrated in several test scripts, especially
  test, test_graphics, and test_stepper.
