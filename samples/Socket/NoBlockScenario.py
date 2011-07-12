"""
NoBlockScenario - each _call immediately followed by _return
"""

from Socket import send_call, send_return, send_close, \
    recv_call, recv_return, recv_close

initial = 0
accepting = (0,2) # consistent with Socket model

# Graph of FSM, list of tuples: (state, action symbol, args, next state)

# Here args are all empty to match any args in model program

graph = ((0, (send_close, (), None), 0), # order actions so no blocking
         (0, (recv_close, (), None), 0), # cant close while send or recv pending
         (0, (send_call, (), None), 1),  # send before recv, call then return
         (1, (send_return, (), None), 2),
         (2, (send_close, (), None), 2),
         (2, (recv_close, (), None), 2),
         (2, (recv_call, (), None), 3), 
         (3, (recv_return, (), None), 0))
