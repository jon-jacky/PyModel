"""
msocket, model program for Python socket library send and recv,
including nondeterminism and concurrency.

This model does not include actions for open, bind, listen, accept,
connect, or close.  To test a real implementation, those must all be
handled in the stepper initialization and reset.

(named msocket not socket to avoid name conflict with Python standard
library socket module)
"""

### Model ###

# State, with initial values
# In our initial state, connection is already open but no send yet

send_arg = str() # send argument waiting to be added to buffers
                # nonempty indicates send_call but not yet send_return

recv_arg = 0  # nonzero indicates recv_call but not yet recv_return

buffers = str() # all messages in flight, models both send and recv buffers

# Accepting state

def Accepting():
    # No send or recv in progress and no messages in flight
    return not send_arg and not recv_arg and not buffers

# Actions. send and recv can block, must model each with separate call, return

# Sender

def send_call_enabled(msg):
    return not send_arg

def send_call(msg):
    global send_arg
    send_arg = msg

def send_return_enabled(n):
    return send_arg and n <= len(send_arg)

def send_return(n):
    # n is the number of chars sent, the return value of socket.send
    global send_arg, buffers
    buffers = buffers + send_arg[:n] # add first n msg chars to end of buffers
    send_arg = str()

# Receiver

def recv_call_enabled(bufsize):
    return not recv_arg

def recv_call(bufsize):
    global recv_arg
    recv_arg = bufsize

def recv_return_enabled(msg):
    n = len(msg)
    return (recv_arg and n <= len(buffers) and msg == buffers[:n] 
            and 0 < n <= recv_arg)

def recv_return(msg):
    # msg is the received data, the return value of socket.recv
    # n is number of bytes actually read, param. gen. assigns nondetermistically
    global recv_arg, buffers
    recv_arg = 0
    n = len(msg)
    buffers = buffers[n:] # remove first n characters from start of buffers


### Metadata

state = ('send_arg', 'recv_arg', 'buffers')

actions = (send_call, send_return, recv_call, recv_return)

cleanup = (send_return, recv_call, recv_return)

enablers = {send_call:(send_call_enabled,),send_return:(send_return_enabled,), 
            recv_call:(recv_call_enabled,),recv_return:(recv_return_enabled,)}

domains = { send_call: {'msg':('a','bb')}, send_return: {'n':(1,2)},
            recv_call: {'bufsize':(4,)}, 
            recv_return: {'msg':('a','b','aa','ab','ba','bb')}}

# Restore initial state, needed by test runner for multiple runs

def Reset():
    global send_arg, recv_arg, buffers
    send_arg = str()
    recv_arg = 0
    buffers = str()
