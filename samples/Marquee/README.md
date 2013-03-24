Marquee 
=======

This sample models a marquee with one line of text scrolling from
right to left.

This sample demonstrates how the size and structure of the data affect
the number of states, how a configuration file can augment or replace
items in the model, and how composition with a scenario machine can
restrict the behavior of a model.

- *Marquee*: model program, defines *Load* and *Shift*, but only
   includes *Shift* in the *actions*.  Initializes model state
   *display* with uninteresting text, a pattern of two characters
   repeated thirteen times: _'* * * * * * * * * * * * * '_

- *DisplayFive*: configuration, redefines *actions* to also include *Load*,
  defines *domains* for *Load* with slightly more interesting text,
  a *pattern* of five characters repeated five times: *'Bye  Bye  Bye  Bye  Bye  '*

- *LoadFirst*: scenario machine, forces the *Load* action to execute
  just once at the beginning of the run.

- *test*: *pmt* executes *Marquee* only, so traces only include *Shift*.

- *test_graphics*: generate graphs of *Marquee*, *LoadFirst*, and *Marquee*
   configured with *DisplayFive*, then that combination composed
   with *LoadFirst*.  Some of the commands are repeated, but modules
   appear on the command line in different orders (to show that
   doesn't matter).

- *test_viewer*: Generate the same output as *test_graphics*, but this
  script is shorter because it uses *pmv* instead of *pma* + *pmg* +
  *dot*

- *fsmpy*, *svg*: directories of output files from *test_graphics* or
   *test_viewer*

You can view the generated *.svg* files in a browser.  Hover the 
pointer over any state bubble to see a tooltip that shows the marquee
display in that state.

- *MarqueeFSM*: the repeating *display* pattern with just two
  characters results in two states.  Only *Select* is enabled.

- *DisplayFiveFSM*: here *Marquee* imports *DisplayFive*.  The
  repeating *pattern* with five characters results in five states.
  *Load* is enabled in every state.

- *LoadFirst*: graph of the scenario machine, shows how the *Load* action 
  executes just once at the beginning of the run.

- *PeriodFiveFSM*: compare to *DisplayFiveFSM*.  Here *Marquee* is
   composed with *LoadFirst, so *Load* only executes once at the
   beginning.

- *DisplayFiveFSM1*, *PeriodFiveFSM1*, *PeriodFiveFSM2*: same as
   *DisplayFiveFSM* and *PeriodFiveFSM*, but modules appear on the *pma*
   (or *pmv*) command line in different order, to show that order
   doesn't matter.  In particular, the configuration module
   *DisplayFive* can appear on the command line before or after
   *Marquee*, the model program it imports.

There is no stepper in this sample.

Revised Mar 2013
