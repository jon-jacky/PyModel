Stack
=====

This sample models a stack. This sample shows how to:

- model return values as action arguments

- write and use strategies to guide testing

- use *StateFilter* to exclude states from being reached by the model

- use composition of a model with a test suite to check that the
  traces in the test suite conform to the model

- use composition with a scenario machine to limit behavior by selecting
  particular action arguments

- use observable actions to get action arguments from a composed
  scenario or test suite rather than the domains defined in the model

The contents are:

- *Stack*: model program.  The return value of the *Pop* action is
  modeled as an argument.  This makes it easy to write its enabling
  condition *PopEnabled* that constrains the return value.

- *test*: test script that executes *Stack* with the default random
   strategy, then with *ActionNameCoverage*, then with
   *StateCoverage*.  (Those strategy modules are in the *pymodel*
   source code directory, not this sample directory.)

- *StackDepthThree*: configuration that defines a *StateFilter* that
   limits stack depth

- *StackOneScenario*: scenario machine that limits actions to
   particular argument values

- *test_graphics*: test script that generates graphs of *Stack* by itself,
  the *StackOneScenario* machine, and *Stack* composed with *StackOneScenario*
  with the *StackDepthThree* configuration.

- *Scenarios*: test suite with several traces, some allowed by the *Stack*
  model program, others not allowed.

- *Observables*: configuration that specifies one particular action is
   an observable action

- *AllObservables*: configuration that specifies all actions are
   observable actions

- *test_scenarios*, *test_observables*: two similar test suites that 
  execute *Stack* composed with *Scenarios*, with no observable actions,
  or with the *Observables* and *AllObservables* scenarios.  They show how
  composition of a model with a test suite checks that the
  traces in the test suite conform to the model: the composed traces end
  in a non-accepting state when the test suite violates the model.  They
  also show how observable actions use action arguments from a composed
  test suite or scenario.

- *test_scenario_graphics*: generate graphs that illustrate the same
  phenomena as *test_scenarios* and *test_observables*

View the generated graphics files in a browser.  Hover the
pointer over any state bubble to see a tooltip that shows the state
variables in that state.

- *StackFSM*: graph of *Stack* model program, first 12 transitions, 
  with action arguments defined in the model program module.

- *StackOneScenario*: graph of *StackOneScenario* scenario machine

- *StackSynchronized*: graph of *Stack* composed with *StackOneScenario*, using
  the *StackDepthThree* configuration

- *ScenariosFSM*: graphs of all the traces in the *Scenarios* test
  suite.  They are not composed with the model program, so they all
  reach an accepting state.

- *ValidateScenarios*: graphs of all the traces in the *Scenarios* test
  suite.  Here they are composed with the model program, so the traces stop
  before the first transition that violates the model.  Only the first trace
  reaches its accepting state.

- *ValidateObservables*: graphs of the traces in the *Scenarios* test
  suite composed with the model program, with the *Observables* configuration.
  Here one of the traces gets further because an observable action gets
  its parameter argument from the composed test suite.

- *ValidateAllObservables*: graphs of the traces in the *Scenarios*
  test suite composed with the model program, with the *Observables*
  configuration.  Here another one of the traces gets all the way to
  an accepting state because all actions are observable, so they get
  their parameter arguments from the composed test suite.

There is no stepper in this sample.

Revised Mar 2013
