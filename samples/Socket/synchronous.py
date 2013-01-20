"""
synchronous - send before recv, each _call immediately followed by _return
"""

from msocket import send_call, send_return, recv_call, recv_return

initial = 0
accepting = (0,) # consistent with msocket model

cleanup = (send_return, recv_call, recv_return)

# Graph of FSM, list of tuples: (state, action symbol, args, next state)
# Here args are all empty to match any args in model program

graph = ((0, (send_call, (), None), 1),  # send before recv, call then return
         (1, (send_return, (), None), 2),
         (2, (recv_call, (), None), 3), 
         (3, (recv_return, (), None), 0))
