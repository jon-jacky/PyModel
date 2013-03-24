cases = [
 ('PowerOn, PowerOff alternate due to enabling conditions',
  'pmt -n 10 PowerSwitch'),

 ('PowerOn, PowerOff alternate, end in non-accepting state',
  'pmt -n 3 PowerSwitch'),

 ('Same as above but add -c cleanup option to reach accepting state',
  'pmt -n 3 -c 3 PowerSwitch'),

 ('Use -a option so only PowerOn action is included, can only execute once',
  'pmt -n 10 -a PowerOn PowerSwitch'),

 ('Use -e option so PowerOff action is excluded, PowerOn can only execute once',
  'pmt -n 10 -e PowerOff PowerSwitch'),

 ('Use -r option for multiple runs, notice run after PowerOn also starts with PowerOn',
  'pmt -n 3 -r 2 PowerSwitch')
]
