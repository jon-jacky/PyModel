"""
stepper.py - common code, utilities for socket steppers
"""

import socket  # Python standard library socket module, OR a simulator

# Default configuration, may rebind below
port = 8080
line_length = 80  # length limit for received messages

def listen():
    """
    Initial setup, runs once
    """
    global listener

    # Server's listener socket
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # get and recv buffer size to print below, just FYI
    rcvbuf = listener.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)

    # Ensure we release listener socket immediately when program exits, 
    #  to avoid socket.error: [Errno 48] Address already in use
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Listen, prepare for clients to connect
    listener.bind(('localhost', port))
    listener.listen(1) 
    print '\nServer listens on localhost port %s with RCVBUF size %s' % (port, rcvbuf)


# Define function for client connect - also used in stepper reset()
def connect():
  global client, server, msg, n, bufsize
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # get and print send buffer size, just FYI
  sndbuf = client.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
  print 'Client creates socket with SNDBUF size %s' % (sndbuf)
  client.connect(('localhost', port))
  print 'Client connects to localhost port %s' % port
  server, addr = listener.accept()
  print 'Server accepts connection from ', addr
  # State needed to remember _call args for __return
  msg = ''
  n = 0
  bufsize = 0

def close():
  global client, server
  client.close()
  server.close()

def reset():
  close()
  connect()

# Start listening and connect the first time
# runs when stepper imports stepper_util
listen()
connect()
