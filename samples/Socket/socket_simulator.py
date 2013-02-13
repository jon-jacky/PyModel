"""
socket_simulator.py

Replacement for the Python standard library socket module to use with
the PyModel socket sample, to demonstrate nondeterminism and blocking
even with small messages.

The simulated socket here nondeterministically sends or receives just
part of the message, no matter how short the message (even just
two characters).   The socket blocks on write when buffers are full, and
the buffers can be made very small, by assigning the bufsize variable.
The default bufsize is 3 characters.

When used with the asynchronous stepper (stepper_a), send (and recv)
are called from different threads in the stepper, so that even if the
call blocks because the buffer is full (or empty), it doesn't block
pmt (the test run).  This enables a blocked send (or recv) call to be
unblocked by a later call to recv (or send).

To use this simulator, just put it in the same directory with your
PyModel socket steppers and rename it (or symlink it) to socket.py.
The steppers will load this simulator instead of the standard library
module.
"""

import random    # for nondeterministic behavior
import threading # for blocking on send/full or recv/empty 

"""
Configure nondeterminism and blocking 

buffers represents client's send buffer, server's receive buffer,
and all the storage in the network between.

All sockets share the *same* buffer - intended to have just one 
client socket and one server socket at a time -
"""
buffers = ''  # initially the buffers are empty
nondet = True # False to send/recv entire msg every time
bufsize = 3   # send blocks when buffer full, recv blocks when empty
e = threading.Event() # initially false, e.wait() to block

# used by steppers, here they are all dummies
AF_INET = 0
SOCK_STREAM = 0
SOL_SOCKET = 0
SO_REUSEADDR = 0
SO_RCVBUF = 0
SO_SNDBUF = 0

class connection(object):
    def __init__(self, *args): pass

    def send(self, msg):
        global buffers
        free = bufsize - len(buffers)
        # send blocks if buffer full
        # Asynch stepper - don't just block here, instead wait for free > 0
        while free <= 0:
            e.wait(1) # 1 second timeout, block without spinning
            free = bufsize - len(buffers)
        # nondeterministically choose prefix of msg to send
        msglen = min(len(msg),free)
        msglen = random.randint(1,msglen) if nondet else msglen
        buffers += msg[:msglen]
        return msglen

    def recv(self, nmax):
        global buffers
        # recv blocks if buffer empty
        while len(buffers) <= 0:
            e.wait(1) # 1 second timeout, block without spinning
        # nondeterministically choose suffix of buffers to recv
        msglen = min(nmax,len(buffers))
        msglen = random.randint(1,msglen) if nondet else msglen
        msg = buffers[:msglen]
        buffers = buffers[msglen:]
        return msg

    def close(self): pass


class socket(connection):

    def __init__(self, *args): 
        connection.__init__(self, *args)

    # client and server can both use these
    def getsockopt(self, *args): return None

    def setsockopt(self, *args): pass
        
    # only client uses this
    def connect(self, *args): pass

    # only server users these
    def bind(self, *args): pass

    def listen(self, *args): pass

    def accept(self, *args):
        c = connection(*args)
        return c, 'nowhere.simulator.org'

