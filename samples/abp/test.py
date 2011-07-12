cases = [
  ('Execute ABP FSM, default RandomStrategy, initial action repeats, subsequent actions can repeat more than 2x',
   'pmt.py -s 9 -n 10 ABP'),

  ('Execute ABP FSM, ActionNameCoverage strategy, initial action does not repeat, subsequent actions do not repeat more than 2x',
   'pmt.py -s 9 -g ActionNameCoverage -n 10 ABP'),

  ('Same as above, except add -c for cleanup to end in accepting state',
   'pmt.py -s 9 -g ActionNameCoverage -n 10 -c 3 ABP'),

  ('Execute ABP FSM, ActionNameCoverage strategy, initial action does not repeat, subsequent actions do not repeat more than 2x',
   'pmt.py -s 4 -g ActionNameCoverage -n 10 -c 3 ABP'),

  ('Use -r option for multiple runs, notice each run starts from initial state',   'pmt.py -s 1 -n 5 -c 3 -r 3 ABP')
]
