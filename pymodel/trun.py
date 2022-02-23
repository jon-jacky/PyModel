#!/usr/bin/env python

import sys
import os

# argv[1] is name of module containing test cases
# dir containing this module must be on PYTHONPATH

if len(sys.argv) != 2:
  print('\nUsage: trun <test_cases_module>\n\n')
  sys.exit()

try:
  test = __import__(sys.argv[1])
except ModuleNotFoundError:
  print('\nCould not find tests file "{}".\n\n'.format(sys.argv[1]))
  sys.exit()

# Test cases are in 'cases', a list of pairs of strings, descrip. and commmand:
# cases = [
#  ('Test PowerOn, PowerOff alternate due to enabling conditions',
#   'pct.py -n 10 PowerSwitch'),
#  ... ]

try:
  for (description, cmd) in test.cases: 
    print(description)
    os.system(cmd)
    print()
except AttributeError:
  print('\nCould not find test cases in "{}".\n\n'.format(sys.argv[1]))
  sys.exit()
