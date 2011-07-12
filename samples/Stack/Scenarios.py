# Scenarios to check against Stack model used as oracle

from Stack import *  # action symbols

testSuite = [
  # allowed, use args from domains in Stack module
  [
     (Push, (1,), None),
     (Push, (2,), None),
     (Pop, (2,), None),
     (Pop, (1,), None),
  ],
  # forbidden, pop args in wrong order
  [
     (Push, (1,), None),
     (Push, (2,), None),
     (Pop, (1,), None),
     (Pop, (2,), None),
  ],
  # should be allowed by enabling conds., but use args not in domains in Stack
  [
     (Push, (1,), None),
     (Push, (3,), None),
     (Pop, (3,), None),
     (Pop, (1,), None),
  ],
  # not allowed, initial transitions not enabled.
  [
     (Pop, (2,), None),
     (Pop, (1,), None),
     (Push, (1,), None),
     (Push, (2,), None),
  ],
]
