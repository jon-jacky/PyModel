
safety
======

This sample shows how to do safety analysis in PyModel: write
*invariants* (safety conditions) that describe safe states, then use
*exploration* to search for unsafe states.  Unsafe states are
indicated in the printed output from *pma* (or *pmv*), and in the
generated FSM and graphics files.

The example here is a microwave oven.  The safety condition is: the
microwave power can only be on when the oven door is closed.

- *unsafe_oven*: model program for an unsafe oven.  The enabling
conditions and action bodies allow traces that can reach an unsafe
state.

- *oven*: model program for a safe oven.  The enabling conditions and
action bodies ensure that traces can only reach safe states.

- *test_graphics*: generates FSMs and graphs from both models.  When
  you run this script, the *pma* program prints the number of unsafe
  states found in each model.

- *fsmpy*, *svg*: directories of output files from *test_graphics*.
  The unsafe states are indicated in these output files.

Examine the generated FSM files (in the *fsmpy* directory).  They are
Python modules (in plain text).

- *unsafe_ovenFSM.py*: FSM generated from *unsafe_oven*. The comments
   at the top indicate *1 unsafe states*. Further down, the *states*
   dictionary reports each state, along with its state variables and
   their values.  Below that, *unsafe* is a list of unsafe states,
   identified by their keys in *states*: *unsafe = [3]* here.

- *ovenFSM.py*: FSM generated from *oven*. The comments at the top
  indicate *0 unsafe states* and the *unsafe* list is empty.

View the generated graphics files (in the *svg* directory) in a browser.
Hover the pointer over any state bubble to see a tooltip that shows
the state variables and their values in that state, to confirm whether
the safety condition is satisfied.  Unsafe states are colored red.

- *unsafe_ovenFSM.svg*: graph of *unsafe_oven*.  The unsafe state
   appears in red.

- *ovenFSM.svg*: graph of *oven*, confirms there are no unsafe states.

There is no stepper in this sample.


Revised Apr 2013
