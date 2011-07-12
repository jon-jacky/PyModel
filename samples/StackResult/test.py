"""
Stack tests
"""

cases = [
  ('Default random strategy, actions repeat',
   'pmt.py -n 10 -s 1 Stack'),

  ('ActionNameCoverage, Push and Pop alternate', 
   'pmt.py -n 10 -s 1 Stack -g ActionNameCoverage'),

  ('StateCoverage, repeat Push',
   'pmt.py -n 10 -s 1 Stack StackDepthTen -g StateCoverage')
]
