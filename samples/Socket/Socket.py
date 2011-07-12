"""
Socket, model Python socket library send and recv

This model assumes the connection is already established in the
initial state, so it does not include actions for open, bind, listen,
accept, connect.  To test a real implementation, those must all be
handled in the stepper initialization and reset.
"""

### Model ###

# State, with initial values
# In our initial state, connection is already open but no send yet

send_arg = str() # send argument waiting to be added to buffers
                # nonempty indicates send_call but not yet send_return
send_closed = False 
exception = str()

recv_arg = 0  # nonzero indicates recv_call but not yet recv_return
recv_closed = False

buffers = str() # all messages in flight, models both send and recv buffers

# Accepting state

def Accepting():
    # No send or recv in progress and no messages in flight, or closed
    return not send_arg and not recv_arg and \
        (not buffers or send_closed or recv_closed)

# Actions. send and recv can block, must model each with separate call, return

# Sender

def send_call_enabled(msg):
    return not send_arg and not send_closed and not exception

def send_call(msg):
    global send_arg
    send_arg = msg

def send_return_enabled(n):
    return send_arg and n <= len(send_arg)

def send_return(n):
    # n is the number of chars sent, the return value of socket.send
    global send_arg, buffers
    buffers = buffers + send_arg[:n]
    send_arg = str()

# Should distinguish two send exceptions
# 'forcibly closed' when receiver closed while send blocking, crash immediately
# 'connection aborted' when receiver closed before send called, send may succeed
# 'forcibly closed' is deterministic but 'connection aborted' is not
# In our synchronous stepper, only 'connection aborted' is possible

def send_exception_enabled(exc):
    return send_arg and recv_closed and exc == 'connection aborted'

def send_exception(exc):
    global exception
    exception = exc
    
def send_close_enabled():
    return not send_closed and not send_arg # no send is in progress

def send_close():
    global send_closed
    send_closed = True

# Receiver

def recv_call_enabled(bufsize):
    return not recv_arg and not recv_closed

def recv_call(bufsize):
    global recv_arg
    recv_arg = bufsize

def recv_return_enabled(n):
    return recv_arg and \
        ((0 < n <= recv_arg and n <= len(buffers)) or (n == 0 and send_closed))

def recv_return(n):
    # msg is the received data, the return value of socket.recv
    # n is number of bytes actually read, param. gen. assigns nondetermistically
    global recv_arg, buffers
    recv_arg = 0
    msg = buffers[:n]
    buffers = buffers[n:]
    return msg

def recv_close_enabled():
    return not recv_closed and not recv_arg # no recv is in progress

def recv_close():
    global recv_closed
    recv_closed = True

### Metadata

state = ('send_arg', 'send_closed', 'exception', 'recv_arg', 
         'recv_closed', 'buffers')

actions = (send_call, send_return, send_exception, send_close, 
           recv_call, recv_return, recv_close)

cleanup = (send_return, recv_call, recv_return, send_close, recv_close,
           send_exception)

enablers = {send_call:(send_call_enabled,),send_return:(send_return_enabled,), 
            send_close:(send_close_enabled,), 
            send_exception:(send_exception_enabled,),
            recv_call:(recv_call_enabled,),recv_return:(recv_return_enabled,),
            recv_close:(recv_close_enabled,) }

domains = { send_call: {'msg':('a','bb')}, send_return: {'n':(1,2)},
            send_exception: {'exc':'connection aborted'},
            recv_call: {'bufsize':(4,)}, recv_return: {'n':(0,1,2,3,4)} }

# Restore initial state, needed by test runner for multiple runs

def Reset():
    global send_arg, send_closed, recv_arg, recv_closed, buffers
    send_arg = str()
    send_closed = False
    exception = str()
    recv_arg = 0
    recv_closed = False
    buffers = str()
