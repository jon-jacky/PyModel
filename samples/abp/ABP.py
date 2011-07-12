"""
Alternating Bit Protocol FSM
"""

# actions

def Send(bit): pass
def Ack(bit): pass

# cleanup actions

cleanup = (Ack,)

# initial state, accepting states

initial = 0
accepting = (0,2,4)

# graph of finite state machine: seq of (current, (action,args,result), next)

graph = ((0, (Send, (1,), None), 0),
       (0, (Ack, (1,), None), 0),
       (0, (Send, (0,), None), 1),
       (1, (Send, (0,), None), 1),
       (1, (Ack, (1,), None), 1),
       (1, (Ack, (0,), None), 2),
       (2, (Ack, (0,), None), 2),
       (2, (Send, (1,), None), 3),
       (3, (Send, (1,), None), 3),
       (3, (Ack, (0,), None), 3),
       (3, (Ack, (1,), None), 4),
       (4, (Ack, (1,), None), 4),
       (4, (Send, (0,), None), 1))
