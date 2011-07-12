"""
Receiver.py, based on echo server at http://docs.python.org/library/socket.html
"""

# import this module to listen on port 8080

import sys
import socket

port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rcvbuf = s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
# mss = s.getsockopt(socket.SOL_IP, socket.TCP_MAXSEG) # SOL_TCP returns 0
# print 'Listen on port %s with RCVBUF %s, MAXSEG %s' % (port, rcvbuf, mss)
print 'Listen on port %s with RCVBUF %s' % (port, rcvbuf)
s.bind(('localhost', port))
s.listen(1) 
conn, addr = s.accept()
print 'Connected by ', addr

# Now can read by repeating data = conn.recv(n) until EOF or connection lost
# Then should conn.close()


