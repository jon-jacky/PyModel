""" 
pymodel configuration: remove nondeterminism, always send/recv entire message
"""

import Socket

def send_all_enabled(n):
    return Socket.send_arg and n == len(Socket.send_arg) # Socket: not n <= ...

def recv_all_enabled(n):
    return (Socket.recv_arg and # in Socket: not n <= len(buffers) but n == ...
            ((0 < n <= Socket.recv_arg and n == len(Socket.buffers)) or (n == 0 and Socket.send_closed)))

Socket.enablers.update({Socket.send_return:(send_all_enabled,),
                        Socket.recv_return:(recv_all_enabled,)})
