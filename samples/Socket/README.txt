
PyModel socket sample: modeling and testing nondeterminism and concurrency

This sample uses network sockets to demonstrate several PyModel
techniques for modeling and testing systems that exhibit
nondeterminism, concurrency, and asynchrony.

To understand the discussion here, you should first read these files
in the notes directory: concepts.txt, models.txt, composition.txt, and
stepper.txt.


Motivation: sockets are nondetermistic and concurrent

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


Socket sample contents

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


Socket model program: modeling nondeterminism and concurrency

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
entire message.  So send or recv might return different values and
update the state differently, even when called in the same state with
the same arguments --- this is the essence of nondeterminism.

In PyModel model programs, nondeterminism is implemented by enabling
conditions.  Each action (for example send_call) has a corresponding
enabling condition (for example send_call_enabled), a boolean function
of the action arguments and the model program state.  The action can
be called whenever the enabling condition is satisfied (returns True).
(If the model program has no explicit enabling condition for an
action, it is taken to be True always --- the action is always
enabled.).  A boolean function can be written to be satisfied by many
different combinations of values, so this provides a way to represent
nondeterminism easily.  PyModel may call the action with any one of
the combinations of arguments that satisfy the enabling condition in
the current state.  PyModel considers all satisfying combinations and
chooses one (at random, or optionally guided by a strategy defined by
the programmer).  Usually the enabling condition can be satisfied by a
large range of argument values, but the actual argument values that
are used must be drawn from a *parameter generator*, a collection
defined by the programmer.  A parameter generator must be defined for
each argument of each action.  The parameter generator might be a
fixed collection that is defined when the model program is written, or
it might be computed from the model program state each time an
argument value is needed.  The parameter generators are defined
separately from the enabling conditions, so they provide a convenient
way to control the potential nondeterminism offered by the enabling
conditions.  An enabling condition might permit a large range of
argument values, but the parameter generator can limit it to a few, or
just one.

It is typical for the enabling conditions and parameter generators to
permit several different actions to be enabled in a given state;
again, PyModel chooses one (at random or according to a programmed
strategy).  In this way, a model program can exhibit nondeterminism
regarding which action is executed, not just which argument values are
used.

Enabling conditions and parameter generators can also represent
nondeterministic outcomes from actions.  This is accomplished by
coding each operation (here, each function call in the implementation)
as *two* actions in the model program.  For example, the send function
in the implementation is represented by send_call and send_return
actions in the model program.  An action modeled in this style, where
the start and finish of the operation (here, the function call and its
return) are coded as two separate actions in the model, is called a
*split action*.  Both start and finish actions in a split action
require an enabling condition (if either is omitted, that part of the
action is considered to be enabled always).  Split actions never have
return values.  Instead, the return value (or values) of the modeled
action are coded as arguments of the finish action.  So where the
implemention has n = c.send(msg) and msg = s.recv(bufsize), the model
has send_call(msg) then send_return(n), and recv_call(bufsize) and
recv_return(msg).  Therefore, nondeterministic action outcomes can be
represented by coding the enabling conditions and parameter generators
for the finish actions.  For example, PyModel can nondeterministically
choose values for n (the number of characters acceped by send) and msg
(the message returned by recv).  The enabling conditions for the
finish actions are the postconditions for those operations --- which
can be nondeterministic, if the programmer desires.

(An alternative way to represent nondeterministic outcomes without
split actions would be to write code in the action body that generates
a collection of possible results, and then randomly choose one.  But
it turns out to be more convenient, flexible, and general to represent
nondeterminism with split actions, enabling conditions, and parameter
generators.  This is the method that is recommended and supported by
PyModel.  In particular, the PyModel analyzer (the pma program) might
overlook nondeterminism that arises in action bodies -- it might omit
some of those nondeterministic outcomes from its analyses.)

The model exhibits concurrency, like a real socket connection.
PyModel represents concurrency by interleaving.  Send and receive
actions can interleave without synchronization at the two ends of the
connection.  Each end can send or receive while the other end is
blocked.  This is achieved by modeling both send and receive as *two*
distinct actions for the call and return: send_call and send_return,
and recv_call and recv_return.  For example, we might see a trace with
these actions:

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

In PyModel, concurrency and interleaving are represented by split
actions.  It is necessary to code split actions in order to model
concurrency where some operations can proceed while others are
blocked.  Behavior that is event-driven, that can occur at
upredictable times, especially where the end of an operation occurs at
some time after the beginning (with other actions occuring in the
meantime), is called *asynchronous* behavior.  Split actions are a way
to code asynchrony in PyModel.  So split actions serve *two* functions
in PyModel.  In addition to representing nondeterminism (explained
above), they also represent concurrency.

(... Consider omitting close actions from the model program discussed
here so we can omit this: ...  In this model, the send and receive
actions are split actions, but the close actions are not split - they
are examples of *atomic actions*.)


Scenarios, parameter generators, and configurations:
controlling nondeterminism and concurrency.

The Socket model program in this sample exhibits nondeterminism and
asynchronous behavior, but these are rarely seen in the common
situation where a socket transmits small messages over a fast network.
In fact, our Stepper module only works correctly with runs that
exhibit these common (deterministic, synchronous) behaviors; it
considers any nondeterminism to be a test failure and just waits
forever at the first blocking call (stepper_o and stepper_a relax
these restrictions).  Therefore, sometimes we wish to restrict the
behavior of the model to deterministic, synchronous behaviors.

The test_viewer script contains several test cases that show
the behavior of the unrestricted model program, and others that
demonstrate techniques for restricting the behavior.

In PyModel, nondeterminism can be restricted by parameter generators.
The model program specifies the argument values used for every action
by its enabling conditions: a boolean function that the arguments must
satisfy.  Recall that when behavior is modeled by split actions, the
arguments of the finish actions (send_return and recv_return here) are
actually the return values -- so the enabling conditions for the
arguments of these actions are actually postconditions on the
operation.  Recall that a boolean function can often be satisfied (made to
return True) by many different values, so this way of modeling
operations represents nondeterminism easily.

In PyModel, concurrency and asychrony permitted by a model program can
be removed by scenario machines.  *NoBlockScenario* is a scenario
machine, an FSM.  Running the test_graphics script causes pma and pmg
to draw the graph of this FSM in the file NoBlockCompose.svg, which
you can view in a browser.  As the graph shows, in this scenario
send_call is always immediately followed by send_return, and recv_call
is always immediately followed by recv_return.  Composing the model
program with this scenario machine has the effect of merging the two
parts of each split action into a single atomic (indivisible) action.
Once send or recv is called, it always returns before another action
can begin - now the behavior is *synchronous*.  Moreover, in this
scenario one send is always followed by one recv - now the behavior is
*sequential*.

