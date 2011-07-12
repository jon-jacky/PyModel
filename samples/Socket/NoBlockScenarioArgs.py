"""
NoBlockScenario - each _call immediately followed by _return
"""

from Socket import * # action symbols

initial = 0
accepting = (0,)

# Graph of FSM, list of tuples: (state, action symbol, args, next state)

# Here args are all empty to match any args in model program

graph = ((0, send_close, (), 0),  # order actions so no blocking
         (0, recv_close, (), 0),  # cannot close while send or recv pending
         (0, send_call, ('a',), 1),   # send before recv, call then return
         (1, send_return, (1,), 2),
         (2, send_close, (), 2),
         (2, recv_close, (), 2),
         (2, recv_call, (4,), 3), 
         (3, recv_return, (1,), 0))
