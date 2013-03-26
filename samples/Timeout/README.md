Timeout
=======

This sample demonstrates the *pmt -t* (that is, *--timeout*) option.

It also shows how a simple test suite can be written to exercise a stepper,
without writing a model program.

- *Stepper*: stepper that implements a *sleep* action by calling the 
  Python standard library *time.sleep* function.

- *Timeout*: test suite for testing *Stepper*.  It has one trace that
  invokes the stepper's *sleep* action three times, with increasingly
  long intervals: 2, 5, and 10 seconds

- *test*: test script that demonstrates the *pmt* timeout option.  It
  has two commands, that execute *pmt* with *Stepper* and *Timeout*,
  first with no *pmt -t* option, then with *-t 7* (seconds).  The
  first run executes all three *sleep* actions to completion.  In the
  second run, while executing the third *sleep* action, pmt* raises
  *TimeoutException* after seven seconds.

Revised Mar 2013
