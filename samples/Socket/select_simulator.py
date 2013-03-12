"""
select_simulator

This module simulates the Python standard library select module.  See
the socket_simulator module header and the Socket sample README for more
explanation.

This module only works with our socket_simulator module - which it
imports. 

This simulated select module is *not* a general purpose replacement
for the Python standard library select module.  It *only* works with
the PyModel Socket sample steppers, where there is only one socket connection 
where the caller only sends at one end and only receives at the other end.

Call select in this module to find out whether the input and/or output
are ready in the simulated socket in the socket_simulator module.  The
first argument, the input list, must be a list of one element: the
simulated recv socket.  The second argument, the output list, must be
a list of of one argument, the simulated send socket.   The call to select
in stepper_s shows how.  

The returned values indicate that input is ready if the simulated
buffer in the socket_simulator module is not empty.  They indicate
output is ready if the simulated buffer is not full.  Again, stepper_s
shows how.

This has to be a separate module from socket_simulator so "import
select" in the stepper modules works as intended: it gets this module
instead of the standard library select module.

To use this simulator, just put it in the same directory with the
PyModel socket stepper modules and the PyModel socket_simulator
module, and rename it (or symlink it) to select.py.  Then the steppers
will load this simulator instead of the Python standard library selec
module.
"""

import socket_simulator # for bufsize 

def select(receivers, senders, exceptions, timeout):
    """
    receivers - list of one element, the simulated receiver socket
    senders - list of one element, the simulated sender socket
    exceptions - empty list, the simulated sockets with exceptions
    ignore timeout - there is no real concurrency here
    """
    # print 'select: recv buffers "%s", send buffers "%s", bufsize %d' % \
    #    (''.join(receivers[0].buffers), ''.join(senders[0].buffers), bufsize) #DEBUG
    inputready = receivers if len(receivers[0].buffers) > 0 else []
    outputready = senders if (socket_simulator.bufsize 
                              - len(senders[0].buffers)) > 0 else []
    exceptions = []
    return inputready, outputready, exceptions
