"""
Sender.py, based on echo client at http://docs.python.org/library/socket.html
"""

# import this module to connect to localhost on port 8080

import sys
import socket

port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sndbuf = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
# mss = s.getsockopt(socket.SOL_IP, socket.TCP_MAXSEG) # SOL_TCP returns 0
# print 'Create socket with SNDBUF %s, MAXSEG %s' % (sndbuf, mss)
print 'Create socket with SNDBUF %s' % (sndbuf)
s.connect(('localhost', port))
print 'Connect to localhost on port %s' % port

# Now can repeat s.send(data) until EOF, then should s.close
