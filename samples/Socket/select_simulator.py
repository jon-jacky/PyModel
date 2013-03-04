"""
select_simulator

Simulated select works with socket_simulator.py 

To use this simulator, just put it in the same directory with your
PyModel socket steppers and rename it (or symlink it) to select.py.
The steppers will load this simulator instead of the standard library
module.
"""

from socket_simulator_s import buffers, bufsize

def select(receivers, senders, exceptions, timeout):
    """
    receivers - list of one element, the simulated receiver socket
    senders - list of one element, the simulated sender socket
    exceptions - empty list, the simulated sockets with exceptions
    """
    # ignore timeout - there is no real concurrency here
    inputready = receivers if len(buffers) > 0 else []
    outputready = senders if bufsize - len(buffers) > 0 else []
    exceptions = 0
    return inputready, outputready, exceptions
