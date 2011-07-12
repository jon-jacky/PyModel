"""pymodel config"""

import Socket

Socket.observables = (Socket.send_call, Socket.send_return, Socket.recv_call,
                       Socket.recv_return, Socket.send_close,Socket.recv_close)
