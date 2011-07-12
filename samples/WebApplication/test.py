"""
WebApplication tests without stepper - fast!
"""

cases = [
 ('WebModel -a option includes only Initialize Action',
  'pmt.py -n 10 -a Initialize WebModel'),

 ('WebModel -e option excludes Login, Logout actions',
  'pmt.py -n 10 -e Login -e Logout WebModel'),

 ('WebModel TestIntSuccess offline test suite',
  'pmt.py TestIntSuccess'),

 ('WebModel on-the-fly with all actions, default random strategy, shows repeated calls to same action',
  'pmt.py -n 10 -s 2 WebModel'),

 ('WebModel on-the-fly with all actions, ActionNameCoverage strategy, shows the same (enabled) action is not repeated more than 2x',
  'pmt.py -n 10 -s 2 WebModel -g ActionNameCoverage'),

 ('WebModel on-the-fly with all actions, StateCoverage strategy, shows Login and UpdateInt actions repeat but with different arguments',
  'pmt.py -n 10 -s 2 WebModel -g StateCoverage'),

 ('WebModel, no -c option, ends in non-accepting state with users logged in',
  'pmt.py -n 10 -s 2 WebModel'),

 ('WebModel, with -c option for cleanup, logs off users to reach accepting state',
  'pmt.py -n 10 -s 2 -c 3 WebModel'),

 ('WebModel, with -r --runs option, in each run Initialize is enabled again',
  'pmt.py -n 5 -s 3 -r 3 WebModel'),

 ('WebModel TestIntTwoRuns offline test suite with two runs',
  'pmt.py TestIntTwoRuns'),
]
