
PyModel samples
===============

There is a directory for each sample, including a *README* with more
information about that sample.  The samples are:


- *abp*: models the *alternating bit protocol*, a simple network
 protocol that retransmits lost or corrupted messages.  This model is
 a Finite State Machine (FSM).  It shows that an FSM can be
 used as the model (not just as a scenario machine).  Just like a
 model program, an FSM can generate traces, generate graphics, and be
 composed with test suites.

- *Marquee*: a marquee with one line of text scrolling from right to
  left.  Demonstrates how the size and structure of the data affect
  the number of states, how a configuration file can augment or
  replace items in the model, and how composition with a scenario
  machine can restrict the behavior of a model.

- *populations*: models a population whose members can be added or
  removed.  It demonstrates state-dependent domains.  Since the
  population is a collection of random elements, it would not be
  possible to define a fixed domain in advance.

- *PowerSwitch*: a very simple model program and an FSM, for an on-off
  power switch and a speed control.  Demonstrates several PyModel
  techniques (including composition) on a minimal example.

- *safety*: models a microwave oven with a safety condition: the
  microwave power can only be on when the oven door is closed.  Shows
  how to do safety analysis in PyModel: write *invariants* (safety
  conditions) that describe safe states, then use *exploration* to
  search for unsafe states.

- *Socket*: uses network sockets to demonstrate several PyModel
  techniques for modeling and testing systems that exhibit
  nondeterminism, concurrency, and asynchrony.  Includes a stepper
  (test harness) for testing the Python standard library *socket*
  module.  Also includes a simulator that can replace the standard
  *socket* module with a substitute that can be configured to exhibit
  failures and demonstrate nondeterminism.

- *Stack*: models a stack.  Shows how to model return values as action
   arguments, write and use strategies to guide testing, use
   *StateFilter* to exclude states from being reached by the model,
   use composition of a model with a test suite to check that the
   traces in the test suite conform to the model, and use observable
   actions to get action arguments from a composed scenario or test
   suite rather than the domains defined in the model.

- *StackResult*: models a stack, in a different style than the *Stack*
   sample.

- *Timeout*: demonstrates the *pmt -t* (that is, *--timeout*) option.
  Shows how a simple test suite can be written to exercise a stepper,
  without writing a model program.

- *tracemultiplexer*: Simulate a program where two threads write to
  the same log file. Exhibit nondeterminism in scheduling threads. Try
  to synchronize so that only one thread at a time can write to the
  log.  Detect unsafe states where both threads may write to the log.
  Identify log messages that may have been corrupted by unsynchronized
  writes from both threads.

- *WebApplication*: contains *WebModel*, a model for a web
  application, *webapp*, an actual web application implementation (in
  Python), and *Stepper*, a stepper that allows the tester *pmt* to use
  the model to drive the web application.  To test, run *webapp* on
  *localhost* using the PyModel *wsgirunner* command.  *Stepper* is a
  web client.  It simulates a browser, sending HTTP requests to the
  web application.

Each sample includes several test scripts: *test.py* etc. To run a
script, type *trun test* etc. (not *python test.py*).  For more
directions on how to run the samples, see also *samples.txt* and
*test.txt* in the *notes* directory.


Revised May 2013



