#!/usr/bin/env python
"""
PyModel Tester
"""

import os
import sys
import imp
import pdb # can optionally run in debugger, see main
import random
import traceback
import TesterOptions

from ProductModelProgram import ProductModelProgram


def SelectAction(enabled):
  """
  Default strategy: choose an enabled action at random
  """
  if enabled:  # might be empty
    (aname, args, result, next, properties) = random.choice(enabled)
    return (aname, args)
  else:
    return (None,None)

# for printing output file
def fmtarg(arg):
  return '%s' % arg # FIXME, quotes around literal strings, print None

def fmtargs(args):
  return '%s' % args # FIXME?
  #return ','.join([ fmtarg(arg) for arg in args ])

def quote(s):
  return "'%s'" % s if isinstance(s, str) else s

def RunTest(options, mp, stepper, strategy, f, krun):
  """
  Execute one test run
  """
  if options.output:
    f.write('  [\n')
  isteps = 0  
  failMessage = None # no failMessage indicates success
  infoMessage = ''
  cleanup = False
  maxsteps = options.nsteps
  while options.nsteps == 0 or isteps < maxsteps:
    # print 'Current state: %s' % mp.Current() # DEBUG
    # execute test run steps.
    # actions identified by aname (string) at this level, for composition
    # EnabledTranstions returns: [(aname,args,result,next,properties),...]
    enabled = mp.EnabledTransitions(cleanup) 
    (aname, args) = strategy.SelectAction(enabled)
    # exit conditions
    if not aname: 
      if not cleanup:
        infoMessage = 'no more actions enabled'
      break   
    elif cleanup and mp.Accepting():
      break
    # execute a step
    else:
      isteps = isteps + 1
      modelResult = mp.DoAction(aname, args) # Execute in model, get result
      qResult = quote(modelResult)
      if modelResult != None:
        print aname if options.quiet else '%s%s / %s' % (aname, args, qResult)
      else:
        print aname if options.quiet else '%s%s' % (aname, args)
      if options.output:
        if qResult != None:
          f.write('    (%s, %s, %s),\n' % (aname, args, qResult))
        else:
          f.write('    (%s, %s),\n' % (aname, args)) # optional missing result
      if stepper:
        # FIXME could add timeout here
        try:
          # Execute action in stepper.
          # Check conformance. If test succeeds, stepper returns None
          failMessage = stepper.TestAction(aname, args, modelResult) 
          # Ignore conformance check if model returned None -- ?
          # failMessage = failMessage if modelResult != None else None
        except BaseException as e:
          traceback.print_exc() # looks just like unhandled exception
          failMessage = 'stepper raised exception: %s, %s' % \
              (e.__class__.__name__, e)
      if failMessage:
        break 
      # end executing a step
    # begin cleanup phase
    if isteps == options.nsteps:
      cleanup = True
      maxsteps += options.cleanupSteps
    # end while executing test run steps

  # Print test run outcome, including explanation and accepting state status
  acceptMsg = 'reached accepting state' if mp.Accepting() else \
                'ended in non-accepting state'
  infoMessage += '%s%s' % (', ' if infoMessage else '', acceptMsg)
  if stepper and not mp.Accepting() and not failMessage:
      failMessage = infoMessage # test run ends in non-accepting state: fail
  if failMessage:
    print '%3d. Failure at step %s, %s' % (krun, isteps, failMessage)
  else:
    print '%3d. %s at step %s%s' % (krun, 'Success' if stepper else 'Finished',
                                   isteps, 
                                   (', %s' % infoMessage) if infoMessage else '')
  if options.output:
    f.write('  ],\n')


def main():       
  (options, args) = TesterOptions.parse_args()

  # args can include model programs, FSMs, test suites
  if not args:
    TesterOptions.print_help()  # must have at least one arg, not optional
    exit()
  else:
    mp = ProductModelProgram(options, args)

  stepper = __import__(options.iut) if options.iut else None
  if stepper:
    # recognize PEP-8 style names (all lowercase) if present
    if hasattr(stepper, 'testaction'):
      stepper.TestAction = stepper.testaction
    if hasattr(stepper, 'test_action'):
      stepper.TestAction = stepper.test_action
    if hasattr(stepper, 'reset'):
      stepper.Reset = stepper.reset

  if options.strategy:
    strategy = __import__(options.strategy)
    if hasattr(strategy, 'selectaction'):
      strategy.SelectAction = strategy.selectaction
    if hasattr(strategy, 'select_action'):
      strategy.SelectAction = strategy.select_action
  else:
    strategy = imp.new_module('strategy') 
    strategy.SelectAction = SelectAction # handle default strategy in same way

  if options.seed:            # NB -s 0 has no effect, by definition!
    random.seed(options.seed) # make calls to random.choice reproducible

  f = None # must be bound when passed to RunTest
  if options.output:
    f = open("%s.py" % options.output, 'w')
    f.write('\n# %s' % os.path.basename(sys.argv[0])) # echo command line ... 
    f.write(' %s\n' % ' '.join(['%s' % arg for arg in sys.argv[1:]])) # ...etc.
    f.write('\n# actions here are just labels, but must be symbols with __name__ attribute\n\n')
    f.writelines([ 'def %s(): pass\n' % aname for aname in mp.anames ])
    f.write('\n# action symbols\n')
    f.write('actions = (%s)\n' % ', '.join([ aname for aname in mp.anames]))
    f.write('\ntestSuite = [\n')

  k = 0
  while k < options.nruns or options.nruns == 0 or mp.TestSuite:
    if k > 0:
      try:
        mp.Reset()
        if options.output:
          f.write('#\n')
      except StopIteration: # raised by TestSuite Reset after last run in suite
        break
      if stepper:
        stepper.Reset()
    RunTest(options, mp, stepper, strategy, f, k)
    k += 1     
  if k > 1:
    print 'Test finished, completed %s runs' % k

  if options.output:
    f.write(']')
    f.close()

if __name__ == '__main__':
    if '-d' in sys.argv or '--debug' in sys.argv: # run in debugger
      pdb.runcall(main)
    else:
      main ()
