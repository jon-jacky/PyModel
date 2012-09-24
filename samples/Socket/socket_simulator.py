"""
socket_simulator.py

Replacement for the Python standard library socket module to use with
PyModel, to demo the behavior of the Socket model and the various
steppers: Stepper, stepper_o, stepper_a.

To use this simulator, just put it in the same directory with your
PyModel socket steppers and rename it (or symlink it) to socket.py.
The steppers will load this simulator instead of the standard library
module.  EXCEPT on systems like Mac and Windows that don't distinguish
case in filenames, you can't put model Socket.py and simulated
implementation socket.py in the same directory.  Instead you must put
socket.py in a different directory and put that directory on
PYTHONPATH.
"""

import random    # for nondeterministic behavior

"""
Configure nondeterminism and blocking 

buffers represents client's send buffer, server's receive buffer,
and all the storage in the network between.

All sockets share the *same* buffer - intended to have just one 
client socket and one server socket at a time -
"""
buffers = ''
nondet = True # False to send/recv entire msg every time
bufsize = 3   # send blocks when buffer full, recv blocks when empty

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
        if free <= 0:
            while True: pass # FIXME - can't we block without spinning?
        # nondeterministically choose prefix of msg to send
        msglen = min(len(msg),free)
        msglen = random.randint(1,msglen) if nondet else msglen
        buffers += msg[:msglen]
        return msglen

    def recv(self, nmax):
        global buffers
        # recv blocks if buffer empty
        if len(buffers) <= 0:
            while True: pass # FIXME - ditto
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

