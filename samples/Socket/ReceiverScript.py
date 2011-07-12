"""
Receeeiver.py, based on echo server at http://docs.python.org/library/socket.html
"""

import sys
import socket

PORT = int(sys.argv[1])
# buff_size = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_IP, socket.TCP_MAXSEG, 4)
s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 16)
rcvbuf = s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
# rcvlowat = s.getsockopt(socket.SOL_IP, socket.SO_RCVLOWAT)#other SOL fail too
mss = s.getsockopt(socket.SOL_IP, socket.TCP_MAXSEG) # SOL_TCP returns 0
s.bind(('localhost', PORT))
s.listen(1) 
conn, addr = s.accept()
print 'Connected by %s with RCVBUF %s, MAXSEG %s' % \
    (addr, rcvbuf, mss)

while True:
    try:
        n = int(raw_input('recv>'))  # block here until user types n or EOF
        data = conn.recv(n) # block here waiting sender
        if not data:
            print 'connection lost'
            break
        print data
    except EOFError:
        print 'EOF'
        break

conn.close()
