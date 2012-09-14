"""
socket_simulator.py

Replacement for the Python standard library socket module to use with
PyModel, to demo the behavior of the Socket model and the various
steppers: Stepper, stepper_o, stepper_a.

To use this simulator, just put it in the same directory with your
PyModel socket steppers and rename it (or symlink it) to socket.py.
The steppers will load this simulator instead of the standard library
module.

This socket simulator exhibits nondeterministic behavior that sockets
can exhibit, but which are difficult to demo on demand.  This
simulator is configurable, so you can select its nondeterministic
behaviors.

The nondeterminism is discussed in the Socket Programming HOWTO at

  http://docs.python.org/howto/sockets.html

"... Now we come to the major stumbling block of sockets - send and
recv operate on the network buffers. They do not necessarily handle
all the bytes you hand them (or expect from them), because their major
focus is handling the network buffers. In general, they return when
the associated network buffers have been filled (send) or emptied
(recv). They then tell you how many bytes they handled. It is your
responsibility to call them again until your message has been
completely dealt with. ... you may wait on a recv forever, because the
socket will not tell you that there’s nothing more to read (for now).
... if your conversational protocol allows multiple messages to be
sent back to back (without some kind of reply), and you pass recv an
arbitrary chunk size, you may end up reading the start of a following
message. ..."

Actual network buffers are usually quite large (for example 32kb) so
it is not very convenient to demonstrate these effects with PyModel.
This simulator allows you to choose any buffer size, even 1, so you
can demonstrate them on small messages.

"""

class socket(object):

    def __init__(self):
        self.buffers = list()

    def getsockopt(self, *args): return None

    def setsockopt(self, *args): pass

    def bind(self, *args): pass

    def listen(self, *args): pass

    def connect(self, *args): pass

    # this does real work

    def accept(self, *args):
        return simulated_socket(), 'nowhere.simulator.org'

    def send(msg):
        # FIXME send everything for now
        self.buffers.append(list(msg))
        return len(msg)

    def recv(nmax):
        # FIXME receive nmax chars for now
        msg = str(self.buffers[:nmax])
        buffers = buffers[nmax:]
