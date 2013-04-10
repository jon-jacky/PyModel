#!/usr/bin/env python

import sys
import os

# argv[1] is name of module containing test cases
# dir containing this module must be on PYTHONPATH

test = __import__(sys.argv[1])

# Test cases are in 'cases', a list of pairs of strings, descrip. and commmand:
# cases = [
#  ('Test PowerOn, PowerOff alternate due to enabling conditions',
#   'pct.py -n 10 PowerSwitch'),
#  ... ]

for (description, cmd) in test.cases: 
  print description
  os.system(cmd)
  print
