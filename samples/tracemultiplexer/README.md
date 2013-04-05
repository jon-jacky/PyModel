
tracemultiplexer
================

This model simulates a multi-threaded program that has been
instrumented to save traces of its API calls in a log.  

When multiple threads are writing the trace log, there can be
nondeterminism in the order in which API calls and returns are made, and
the order they appear in the trace log.  The purpose of this sample is
to demonstrate that nondeterminism.

More details appear in the tracemultiplexer comment header.

- *tracemultiplexor*: simulates a multi-threaded program that has been
  instrumented to save traces of its API calls in a log. 

- *tracenolock* - like *tracemultiplexer* but no synchronization on trace lock.
  We simply commented out the check for free trace lock in *start_enabled* and
  *finish_enabled*

- *test_graphics* - generate a graph that shows the behavior of *tracemultiplexer*

- *test_nolock_graphics* - generate a graph that shows the behavior of
   *tracenolock*

- *fsmpy*, *svg* - directories of output from the test scripts

View the generated graphics files in a browser.  Hover the
pointer over any state bubble to see a tooltip that shows the state
variables in that state.

- *tracemultiplexerFSM* - graph that shows the behavior of *tracemultiplexer*

- *tracenolock* - graph that shows the behavior of *tracenolock*

There is no stepper in this sample.


Revised Apr 2013
