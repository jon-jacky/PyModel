
tracemultiplexer
================

This model simulates a multi-threaded program that has been
instrumented to save traces of its API calls in a log.  

When multiple threads are writing the trace log, there can be
nondeterminism in the order in which API calls and returns are made, and
the order they appear in the trace log.  The purpose of this sample is
to demonstrate that nondeterminism.

More details appear in the *tracemultiplexer* comment header.

- *tracemultiplexer*: simulates a multi-threaded program that has been
  instrumented to save traces of its API calls in a log. 

- *test_graphics* - generate a graph that shows the behavior of *tracemultiplexer*

- *fsmpy*, *svg* - directories of output from the test scripts

View the generated graphics file in a browser.  Hover the
pointer over any state bubble to see a tooltip that shows the state
variables in that state.

- *tracemultiplexerFSM* - graph that shows the behavior of *tracemultiplexer*

There is no stepper in this sample.


Revised Apr 2013
