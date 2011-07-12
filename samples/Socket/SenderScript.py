"""
Sender.py, based on echo client at http://docs.python.org/library/socket.html
"""

import sys
import socket

PORT = int(sys.argv[1])
# buff_size = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_IP, socket.TCP_MAXSEG, 4)
s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 16)
sndbuf = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
# sndlowat = s.getsockopt(socket.SOL_IP, socket.SO_SNDLOWAT)#other SOL fail too
mss = s.getsockopt(socket.SOL_IP, socket.TCP_MAXSEG) # SOL_TCP returns 0
s.connect(('localhost', PORT))
print 'Connected to port %s with SNDBUF %s, MAXSEG %s' % \
    (PORT, sndbuf, mss)

while True:
    try:
        data = raw_input('send>')  # block here until user types data or EOF
    except EOFError:
        print 'EOF'
        break
    try:
        s.send(data) # may block here, depending on receiver
    except:
        print 'Send failed'
        break

s.close()
