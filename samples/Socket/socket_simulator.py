"""
socket_simulator.py

Replacement for the Python standard library socket module to use with
the PyModel Socket sample, to demonstrate nondeterminism and blocking
even with small messages.

This simulated socket module is *not* a general purpose replacement
for the Python standard library socket module.  It *only* works with
the PyModel Socket sample steppers, where there is only one socket connection 
where the caller only sends at one end and only receives at the other end.

The simulated socket here may nondeterministically send or receive just
part of the message, no matter how short the message (even just two
characters).

The simulated socket here blocks on send when the buffer is full, and
blocks on recv when the buffer is empty.  The buffer can be made very
small, by assigning the bufsize variable.  The default bufsize is 3
characters.

Note that this *same* socket simulator can be used with stepper_a.py,
which achieves asynchrony with threads, and stepper.py which achieves
asynchrony with select.  When stepper.py imports this socket_simulator,
stepper.py must also import select_simulator.

This socket simulator can also be used with the synchronous stepper,
but it may block -- just like a real socket.

To use this simulator, just put it in the same directory with your
PyModel socket steppers and rename it (or symlink it) to socket.py.
The steppers will load this simulator instead of the Python standard
library socket module.
"""

import random    # for nondeterministic behavior
import threading # event e for blocking on send/full or recv/empty 

e = threading.Event() # initially false, e.wait() to block

nondet = True # False to send/recv entire msg every time

# used by steppers, here they are all dummies
AF_INET = 0
SOCK_STREAM = 0
SOL_SOCKET = 0
SO_REUSEADDR = 0
SO_RCVBUF = 0
SO_SNDBUF = 0

# buffers represents client's send buffer, server's receive buffer,
#  and all the storage in the network between.
# Shared buffers is a mutable list that is updated, 
#  not an immutable string that is assigned then reassigned.
# See explanation in socket __init__.
buffers = list('')  # mutable list, not immutable string
bufsize = 3   # send blocks when buffer full, recv blocks when empty

# set errors > 0 to simulate faulty/noisy connection, small means more errors
errors = 5  # characters in recv msg will be altered, with probability 1/errors

class socket(object):

    def __init__(self, *args): 
        """
        The shared buffer has to be a shared mutable variable because the
        only way that the simulated select can access the shared buffer is through its
        passed arguments, the lists of input and output channels.  These
        channels have to be objects and they have to both reference the same
        shared buffer.  Therefore the buffer has to be a shared structure that
        is updated, not an immutable string that is assigned, then reassigned.
        """
        self.buffers = buffers  # all instances have reference to same global buffers
    
    def send(self, msg):
        """
        send must block if buffer full
        so select must ensure that send is not called if buffer is full
        """
        free = bufsize - len(self.buffers)
        # print 'send: msg "%s", buffers "%s", bufsize - len(self.buffers) %d' % \
        #    (msg, ''.join(self.buffers), free) #DEBUG
        # assert free > 0 # in stepper_s, select ensures send is not called if buffer is full
        while free <= 0:
            e.wait(1) # 1 second timeout, block without spinning
            free = bufsize - len(buffers)
        # nondeterministically choose prefix of msg to send
        nmax = min(len(msg),free)
        nsent = random.randint(1,nmax) if nondet else nmax
        # print 'send: nsent %d' % nsent
        self.buffers.extend(list(msg[:nsent])) # mutate list of characters
        return nsent

    def recv(self, nmax):
        """
        recv must block if buffer empty
        so select must ensure that send is not called if buffer is empty
        """
        global buffers
        #print 'recv: buffers "%s", len(self.buffers) %d' % \
        #   (''.join(self.buffers), len(self.buffers)) #DEBUG 
        # assert len(self.buffers) > 0 # in stepper_s, select ensures recv is not called if buffer is empty 
        while len(buffers) <= 0:
            e.wait(1) # 1 second timeout, block without spinning
        # nondeterministically choose suffix of buffers to recv
        msglen = min(nmax,len(self.buffers))
        msglen = random.randint(1,msglen) if nondet else msglen
        msglist = self.buffers[:msglen] # list of characters in msg
        del self.buffers[:msglen] # mutate buffers, list of characters
        # simulate errors, garble the returned msg
        if errors:
            msglist = [ 'X' if (random.random() < 1.0/errors) else c 
                        for c in msglist ]
        msg = ''.join(msglist) # turn list of chars back to string
        return msg

    def close(self): pass

    # client and server can both use these
    def getsockopt(self, *args): return None

    def setsockopt(self, *args): pass
        
    # only client uses this
    def connect(self, *args): pass

    # only server users these
    def bind(self, *args): pass

    def listen(self, *args): pass

    def accept(self, *args):
        return self, 'nowhere.simulator.org'
