"""
Test runs with sequences of blocking calls represented by split actions.
Should be permitted by model, but can't be executed by synchronous stepper.

These runs use domains defined in send_aa
"""

from Socket import *

#n1 = 1
#n2 = 2

# large enough to block on send
n1 = 2**18
n2 = 2*n1

a = 'a'*n1
aa = 'a'*n2

testsuite = [

    # Based on session in two windows where both ends occassionally block
    #
    # >>> s.send('a'*(2**19))
    # 524288
    #(etc.)
    #
    # >>> axxx = conn.recv(2**18)
    # >>> axxx = conn.recv(2**18)
    # (etc.)
    #
    # Here aa and 2 are surrogages for 'a'*(2**19) and 2**19 etc.
    [
        (send_call, (aa,)),
        (send_return, (n2,)),
        (send_call, (aa,)),
        # sender blocks here
        (recv_call, (n1,)),
        (recv_return, (a,)),
        (recv_call, (n1,)),
        (recv_return, (a,)),
        (send_return, (n2,)),
        (send_close, ()),
        (recv_close, ()),
        ]
]
