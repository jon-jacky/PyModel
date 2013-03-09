"""
We need to put select in a separate module so "import select" works

To use this simulator, just put it in the same directory with your
PyModel socket steppers and rename it (or symlink it) to select.py.
The steppers will load this simulator instead of the standard library
module.
"""

import socket_simulator

def select(receivers, senders, exceptions, timeout):
    """
    receivers - list of one element, the simulated receiver socket
    senders - list of one element, the simulated sender socket
    exceptions - empty list, the simulated sockets with exceptions
    """
    # ignore timeout - there is no real concurrency here
    # print 'select: recv buffers "%s", send buffers "%s", bufsize %d' % \
    #    (''.join(receivers[0].buffers), ''.join(senders[0].buffers), bufsize) #DEBUG
    inputready = receivers if len(receivers[0].buffers) > 0 else []
    outputready = senders if (socket_simulator.bufsize 
                              - len(senders[0].buffers)) > 0 else []
    exceptions = []
    return inputready, outputready, exceptions
