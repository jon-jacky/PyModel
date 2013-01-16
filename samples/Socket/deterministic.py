""" 
pymodel configuration: remove nondeterminism, always send/recv entire message

Use state-dependent domains to remove nondeterminism from socket model.
These domains ensure that send always accepts the entire send_arg,
and recv always returns entire buffers.

This only works with import socket then socket.send_arg ... etc.
This does *not* work with from socket import send_arg ... etc.
"""

import socket

socket.domains.update(
    { socket.send_return: { 'n': (lambda: [ len(socket.send_arg) ]) },
      socket.recv_return: { 'msg': (lambda: [ socket.buffers ]) }}) 
