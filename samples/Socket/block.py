"""
Test runs with sequences of blocking calls represented by split actions.
Blocking occurs whenever _call is not immediately followed by its _return

These runs use domains defined in send_aa.py configuration file
"""

from Socket import *

#n1 = 1
#n2 = 2

# large enough to block on send
n1 = 2**18
n2 = 2*n1

a = 'a'*n1
aa = 'a'*n2

observables = (send_return, recv_return)

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
        # sender unblocks here

        (recv_call, (n1,)),
        (recv_return, (a,)),
        (recv_call, (n1,)),
        (recv_return, (a,)),
        (recv_call, (n1,)),
        # receiver blocks here

        
        (send_call, (aa,)),
        (send_return, (n2,)),
        (recv_return, (a,)),
        # receive unblocks here

        (send_close, ()),
        (recv_close, ()),
        ]
]
