"""
Test sockets with increasingly larger messages to find how large
message must be so it is no longer completely transmitted by one send
(so send and recv non longer behave deterministicaly).
"""

# actions here are just labels, but must be symbols with __name__ attribute

from Socket import *

# action symbols
actions = (send_return, send_call, recv_close, send_close, recv_call, send_exception, recv_return)

testsuite = [

  # Deliberate failure on 16-char message
  [
    (send_call, ('a'*16,), None),
    (send_return, (16,), None),
    (recv_call, (16,), None),
    (recv_return, (16,), 'a'*15 + 'b'), # failure expected, wrong char at end
    (send_close, (), None),
    (recv_close, (), None),
  ],

  # Deliberate failure on 8192-char message
  [
    (send_call, ('a'*8192,), None),
    (send_return, (8192,), None),
    (recv_call, (8192,), None),
    (recv_return, (8192,), 'a'*8191 + 'b'), # fail here, wrong char at end
    (send_close, (), None),
    (recv_close, (), None),
  ],

  # Intended success on 8192-char message
  [
    (send_call, ('a'*8192,), None),
    (send_return, (8192,), None),
    (recv_call, (8192,), None),
    (recv_return, (8192,), 'a'*8192),
    (send_close, (), None),
    (recv_close, (), None),
  ],

  # Intended success on 16384-char message
  [
    (send_call, ('a'*16384,), None),
    (send_return, (16384,), None),
    (recv_call, (16384,), None),
    (recv_return, (16384,), 'a'*16384),
    (send_close, (), None),
    (recv_close, (), None),
  ],

  # We omit None return value in following runs

  # Intended success on 32K-char message
  [
    (send_call, ('a'*2**15,)),
    (send_return, (2**15,)),
    (recv_call, (2**15,)),
    (recv_return, (2**15,), 'a'*2**15),
    (send_close, ()),
    (recv_close, ()),
  ],

  # Intended success on 64K-char message
  [
    (send_call, ('a'*2**16,)),
    (send_return, (2**16,)),
    (recv_call, (2**16,)),
    (recv_return, (2**16,), 'a'*2**16),
    (send_close, ()),
    (recv_close, ()),
  ],

  # Intended success on 128K-char message
  [
    (send_call, ('a'*2**17,)),
    (send_return, (2**17,)),
    (recv_call, (2**17,)),
    (recv_return, (2**17,), 'a'*2**17),
    (send_close, ()),
    (recv_close, ()),
  ],
]
