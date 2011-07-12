# Scenarios to check against PowerSwitch model used as oracle

from PowerSwitch import PowerOn, PowerOff

testSuite = [
  # Run 1  - allowed, ends in accepting state
  [
     (PowerOn, (), None),
     (PowerOff, (), None),
     (PowerOn, (), None),
     (PowerOff, (), None)
  ],
  # Run 2  - allowed, ends in non-accepting state
  [
     (PowerOn, (), None),
     (PowerOff, (), None),
     (PowerOn, (), None)
  ],
  # Run 3  - Not allowed, last action not enabled in model
  [
     (PowerOn, (), None),
     (PowerOff, (), None),
     (PowerOn, (), None),
     (PowerOn, (), None)
  ],
  # Run 4  - Not allowed, first action not enabled in model
  [
     (PowerOff, (), None),
     (PowerOff, (), None),
     (PowerOn, (), None),
     (PowerOff, (), None)
  ]
]
