
tracemultiplexer
================

Simulate a program where two threads write to the same log
file. Exhibit nondeterminism in scheduling threads. Try to synchronize
so that only one thread at a time can write to the log.  Detect unsafe
states where both threads may write to the log.  Identify log messages
that may have been corrupted by unsynchronized writes from both
threads.

More details appear in the *tracemultiplexer* comment header.

- *tracemultiplexer*: model program that simulates a multi-threaded
  program with and without synchronization

- *unsynchronized*: configuration that causes *tracemultiplexer* to
  run without synchronization

- *test_viewer*: Generate a graph that shows the behavior of
  *tracemultiplexer* using a lock to synchronize write access to the
  log file, and a second graph showing the behavior of
  *tracemultiplexer* with the *unsynchronized* configuration that
  ignores the lock.

- *fsmpy*, *svg*: directories of output from *test_viewer*

View the generated *.svg* files in a browser.  Hover the pointer over
any state bubble to see a tooltip that shows the state variables in
that state.  

The *log* variable represents the log file: it is a list of tuples
where each tuple represents a log message.  Messages that end with
*'XXX'* were logged when both threads may have written to the log,
so the message may have been corrupted by unsynchronized writes.

- *tracemultiplexerFSM*: graph that shows the behavior of *tracemultiplexer*
  using the lock.  None of the states in this graph are unsafe.  None of the 
  log messages are marked with *'XXX'*.  

- *unsynchronizedFSM*: graph that shows the behavior of *tracemultiplexer*
  ignoring the lock.  There are many more transitions and states in this
  graph because the threads are unsynchronized, so many more interleavings are
  possible.  There are many unsafe states (colored red) where both threads may
  write to the log.  In every unsafe state, the most recently written message in 
  *log* ends with *'XXX'* to indicate it may have been corrupted by 
  unsynchronized writes.  These corrupted messages persist in *log* in
  subsequent states.

There is no stepper in this sample.


Revised Apr 2013
