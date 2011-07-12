"""
WebApplication tests *with* stepper

There must be a web application running with the same url and page names
as in Stepper.py or (optionally) Config.py.  The easiest way is to 
run webapp.py in this sample with the wsgirunner server:

  wsgirunner.py -p 8080 webapp

then you can run this test script.
"""

cases = [
 ('Test: WebModel on-the-fly ends in accepting state, should succeed',
   'pmt.py -n 3 -s 5 -i Stepper WebModel'),

 ('Test: WebModel on-the-fly ends in non-accepting state, should fail',
   'pmt.py -n 3 -s 2 -i Stepper WebModel'),

 ('Test: TestIntSuccess offline test suite, with Stepper, should succeed',
  'pmt.py TestIntSuccess -i Stepper'),

 ('Test: TestIntFailure offline test suite, with Stepper, should fail',
  'pmt.py TestIntFailure -i Stepper'),

 ('Test: TestLoginFiveFailures offline test suite, with Stepper, should succeed',
  'pmt.py TestLoginFiveFailures -i Stepper'),

 ('Test: WebModel on-the-fly with all actions, with Stepper, should fail',
  'pmt.py -n 20 -s 1 -i Stepper WebModel'),

 ('WebModel TestIntTwoRuns offline test suite with two runs',
  'pmt.py TestIntTwoRuns -i Stepper')
]
