# Scenarios to check against ABP FSM used as oracle

from ABP import Send, Ack  # action symbols

testSuite = [
  # Allowed
  [
    (Send, (0,), None),
    (Ack, (0,), None),
    (Send, (1,), None),
    (Ack, (1,), None),
    (Send, (0,), None),
    (Ack, (0,), None)
  ],
  # Forbidden, Send wrong bit after Ack
  [
    (Send, (0,), None),
    (Ack, (0,), None),
    (Send, (1,), None),
    (Ack, (1,), None),
    (Send, (1,), None), # Forbidden! Should be Send, (0,)
    (Ack, (0,), None)
  ]
]
