Marquee 
=======

This sample models a marquee with one line of text scrolling from
right to left.

- *Marquee*: model program, defines *Load* and *Shift*,
   but only includes *Shift* in the *actions*.  Initializes
   model state *display* with uninteresting text.

- *DisplayFive*: configuration, redefines *actions* to include *Load*,
  defines domain for *Load* with more interesting *pattern* argument.
   
- *LoadFirst*: scenario machine, forces the *Load* action to execute
  just once at the beginning of the run.

- *test*: *pmt* executes *Marquee* only, so traces only include *Shift*.

- *test_graphics*: *pma* explores *Marquee*, *LoadFirst*, and *Marquee*
   configured with *DisplayFive*, then that combination composed
   with *LoadFirst*.  Some of the commands are repeated, but modules
   appear on the command line in different orders (to show that
   doesn't matter).

- *fsmpy*, *svg*: directories of output files from *test_graphics*

There is no stepper in this sample.

Revised Mar 2013
