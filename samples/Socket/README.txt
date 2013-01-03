
PyModel socket sample

This sample uses network sockets to demonstrate several PyModel
techniques for modeling and testing systems that exhibit
nondeterminism and concurrency.


Motivation

Socket behavior can be more complicated than expected, because data
are buffered on each end, and may be transported through the network
in an irregular way.  A call to send a message may block until space
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

- A model program Socket that can exhibit nondeterminism and the
  effects of concurrency.

- Several scenario machines and configuration files that select
  particular behaviors of the model program.

- Three steppers: Stepper, stepper_o, and stepper_a that use
  the model program and scenarios to test actual sockets on localhost
  (via the Python standard socket library).

- Two simulators: socket_simulator and socket_simulator_a that can
  optionally replace the Python standard socket library in the
  steppers.  These simulators can be configured to demonstrate a great
  deal of nondeterminism and concurrency, even with small messages.

- Several test scripts that invoke various combinations of these
  modules.


Model program

The model program in the Socket models *both* ends of the connection.
One end of the connection is always the sender and the other end is
always the receiver: all send actions occur at one end and all recv
actions occur at the other.  Messages sent at one end can be
eventually received at the other.  

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
we might see this sequence: 

 ...
 send_call
 recv_call
 recv_return
 send_return
 ...

This could happen where the sender blocks because buffers are full, then
the receiver reads some data, making space available in the buffers, so 
the sender can write some data and return.  Here the sender is blocked from 
send_call through send_return.

