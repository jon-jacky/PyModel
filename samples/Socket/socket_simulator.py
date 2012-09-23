"""
socket_simulator.py

Replacement for the Python standard library socket module to use with
PyModel, to demo the behavior of the Socket model and the various
steppers: Stepper, stepper_o, stepper_a.

To use this simulator, just put it in the same directory with your
PyModel socket steppers and rename it (or symlink it) to socket.py.
The steppers will load this simulator instead of the standard library
module.
"""

# needed by steppers, there they are dummies
AF_INET = 0
SOCK_STREAM = 0
SOL_SOCKET = 0
SO_REUSEADDR = 0

# maybe we could use these to set simulated buffer sizes
SO_RCVBUF = 0
SO_SNDBUF = 0

class connection(object):
    """
    Basic data and methods for both client and server sockets
    This is a separate class because the server socket makes
    one of these for each accept call.
    """
    def __init__(self, *args):
        """
        buffers represents client's send buffer, server's receive buffer,
         and all the storage in the network between
        """
        self.buffers = ''

    def send(self, msg):
        # FIXME send everything for now
        self.buffers += msg
        return len(msg)

    def recv(self, nmax):
        # FIXME receive nmax chars for now
        msg = self.buffers[:nmax]
        self.buffers = self.buffers[nmax:]

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

