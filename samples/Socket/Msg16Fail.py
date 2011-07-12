
# actions here are just labels, but must be symbols with __name__ attribute

from Socket import *

# action symbols
actions = (send_return, send_call, recv_close, send_close, recv_call, send_exception, recv_return)

testSuite = [
  [
    (send_call, ('a'*16,), None),
    (send_return, (16,), None),
    (recv_call, (16,), None),
    (recv_return, (16,), 'a'*15 + 'b'), # failure expected, wrong char at end
    (send_close, (), None),
    (recv_close, (), None),
  ],
]
