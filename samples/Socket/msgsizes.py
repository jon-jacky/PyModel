"""
Test sockets with increasingly larger messages to find how large
message must be so it is no longer completely transmitted by one send
(so send and recv non longer behave deterministicaly).
"""

from msocket import *

# action symbols
actions = (send_return, send_call, recv_call, recv_return)

testsuite = [

  # Deliberate failure on 16-char message
  [
    (send_call, ('a'*16,), None),
    (send_return, (16,), None),
    (recv_call, (16,), None),
    (recv_return, ('a'*15 + 'b',), None), # failure expected, wrong char at end
  ],

  # Deliberate failure on 8192-char message
  [
    (send_call, ('a'*8192,), None),
    (send_return, (8192,), None),
    (recv_call, (8192,), None),
    (recv_return, ('a'*8191 + 'b',), None), # fail here, wrong char at end
  ],

  # Intended success on 8192-char message
  [
    (send_call, ('a'*8192,), None),
    (send_return, (8192,), None),
    (recv_call, (8192,), None),
    (recv_return, ('a'*8192,), None),
  ],

  # Intended success on 16384-char message
  [
    (send_call, ('a'*16384,), None),
    (send_return, (16384,), None),
    (recv_call, (16384,), None),
    (recv_return, ('a'*16384,), None),
  ],

  # We omit None return value in following runs

  # Intended success on 32K-char message
  [
    (send_call, ('a'*2**15,)),
    (send_return, (2**15,)),
    (recv_call, (2**15,)),
    (recv_return, ('a'*2**15,)),
  ],

  # Intended success on 64K-char message
  [
    (send_call, ('a'*2**16,)),
    (send_return, (2**16,)),
    (recv_call, (2**16,)),
    (recv_return, ('a'*2**16,)),
  ],

  # Intended success on 128K-char message
  [
    (send_call, ('a'*2**17,)),
    (send_return, (2**17,)),
    (recv_call, (2**17,)),
    (recv_return, ('a'*2**17,)),
  ],


  # Intended success on 256K-char message
  [
    (send_call, ('a'*2**18,)),
    (send_return, (2**18,)),
    (recv_call, (2**18,)),
    (recv_return, ('a'*2**18,)),
  ],


  # Intended success on 512K-char message
  [
    (send_call, ('a'*2**19,)),
    (send_return, (2**19,)),
    (recv_call, (2**19,)),
    (recv_return, ('a'*2**19,)),
  ],

  # Intended success on 1024K-char (1M-char) message
  [
    (send_call, ('a'*2**20,)),
    (send_return, (2**20,)),
    (recv_call, (2**20,)),
    (recv_return, ('a'*2**20,)),
  ],

  # Intended success on 128K-char message 
  # where recv only gets 64K - this can really happen,
  # should be permitted by model
  [
    (send_call, ('a'*2**17,)),
    (send_return, (2**17,)),
    (recv_call, (2**17,)),
    (recv_return, ('a'*2**16,)),
  ],
]
