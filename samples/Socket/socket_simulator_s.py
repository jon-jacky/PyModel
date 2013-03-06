"""
socket_simulator_s.py

Socket simulator that works with stepper_s that uses select.
This socket_simulator works with select_simulator.

Replacement for the Python standard library socket module to use with
the PyModel socket sample, to demonstrate nondeterminism and blocking
even with small messages.

The simulated socket here nondeterministically sends or receives just
part of the message, no matter how short the message (even just
two characters).   

(?) The socket blocks on write when buffers are full, and
the buffers can be made very small, by assigning the bufsize variable.
The default bufsize is 3 characters.

...

To use this simulator, just put it in the same directory with your
PyModel socket steppers and rename it (or symlink it) to socket.py.
The steppers will load this simulator instead of the standard library
module.
"""

import random    # for nondeterministic behavior

"""
Configure nondeterminism and blocking 

buffers represents client's send buffer, server's receive buffer,
and all the storage in the network between.

All sockets share the *same* buffer - intended to have just one 
client socket and one server socket at a time -
"""

nondet = True # False to send/recv entire msg every time

def select(receivers, senders, exceptions, timeout):
    """
    receivers - list of one element, the simulated receiver socket
    senders - list of one element, the simulated sender socket
    exceptions - empty list, the simulated sockets with exceptions
    """
    # ignore timeout - there is no real concurrency here
    print 'select: recv buffers "%s", send buffers "%s", bufsize %d' % \
        (''.join(receivers[0].buffers), ''.join(senders[0].buffers), bufsize) #DEBUG
    inputready = receivers if len(receivers[0].buffers) > 0 else []
    outputready = senders if bufsize - len(senders[0].buffers) > 0 else []
    exceptions = []
    return inputready, outputready, exceptions


# used by steppers, here they are all dummies
AF_INET = 0
SOCK_STREAM = 0
SOL_SOCKET = 0
SO_REUSEADDR = 0
SO_RCVBUF = 0
SO_SNDBUF = 0


# buffers has to be one mutable object so it can be shared by send and recv 
buffers = list('')  # list is mutable
bufsize = 3   # send blocks when buffer full, recv blocks when empty

class socket(object):
    def __init__(self, *args): 
        self.buffers = buffers  # all instances have reference to same global buffers
    
    def send(self, msg):
        """
        send must block if buffer full
        so select must ensure that 
        send is not called if buffer is full:
        """
        free = bufsize - len(self.buffers)
        print 'send: buffers "%s", bufsize - len(self.buffers) %d' % \
            (''.join(self.buffers), free) #DEBUG
        assert free > 0 # send is not called if buffer is full
        # nondeterministically choose prefix of msg to send
        msglen = min(len(msg),free)
        msglen = random.randint(1,msglen) if nondet else msglen
        self.buffers.extend(list(msg[:msglen])) # mutate list of characters
        return msglen

    def recv(self, nmax):
        """
        recv must block if buffer empty
        so select must ensure that 
        send is not called if buffer is empty
        """
        global buffers
        print 'recv: buffers "%s", len(self.buffers) %d' % \
            (''.join(self.buffers), len(self.buffers)) #DEBUG
        assert len(self.buffers) > 0 # recv is not called if buffer is empty
        # nondeterministically choose suffix of buffers to recv
        msglen = min(nmax,len(self.buffers))
        msglen = random.randint(1,msglen) if nondet else msglen
        msg = ''.join(self.buffers[:msglen]) # make string from part of list
        del self.buffers[:msglen] # mutate list of characters
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

# for debugging select, above

if __name__ == '__main__':
    c = connection()
    select([c],[c],[],0)
    c.buffers = 'a'
    select([c],[c],[],0)
    c.buffers = 'ab'
    select([c],[c],[],0)
