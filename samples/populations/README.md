populations
===========

This sample models a population whose members can be added or removed.
It demonstrates state-dependent domains.

There is one state variable *population*, a set.  In these examples
all of the elements of the set are integers.  (A *set* is a collection
without duplicates and without order; *set* is a class in the Python
*builtin* module.)  There are two actions, *add* and *remove*, each
with one argument: the element to be added or removed.

The domains for each action that are defined in the *populations*
module are not fixed collections; they are lambda expressions that are
evaluated each time the action might be invoked.  Making them callable
forces their re-evaluation each time.  The domain for *add* evaluates
to a list containing a single random integer (which is different each
time the domain is evaluated).  The domain for *remove* evaluates to
the *population* set itself, so any argument chosen from this domain
is guaranteed to be present in the population.  Since the population
is a collection of random elements, it would not be possible to
define a fixed domain in advance.  

The *domains9* configuration module redefines the domains as functions
(not lambda expressions), which also works.  The *domainsx*
configuration redefines the domains as collections (not callables),
which does not work --- they are not re-evaluated each time they are
used, but are evaluated only once when the module is imported.

The modules in this sample are:

- *populations*: model program, includes state-dependent domains
  defined using lambda expressions.

- *domains9*: configuration module that redefines domains using
   functions (not lambda expressions).  This also works.

- *domainsx*: configuration module that redefines domains using
   collections (not functions or lambda expressions).  This does not
   work.

- *filter3*: configuration module that defines a *StateFilter* that
  limits the population to no more than three elements.
  
- *filter3_lc*: like *filter3*, except *statefilter* is spelled with
   all lowercase letters, as recommended in the Python style guide,
   PEP8.  This works too.

- *test*: one short run of the model program.

- *test_filter*: first, a run without any state filter to show how the
   population can grow, then runs with both state filters to show
   they both limit the population to no more than three elements.

- *test_domains*: first, a run with the domains defined in the model
  program, to show the element values can range up to 99, then runs
  with both domain configurations to show the element values only
  range up to 9.

- *test_domainsx*: a run that shows *domainsx* does not work (the domain
  is not a callable)

- *test_seed*: demonstrate the *-s* (seed) option to *pmt*, which
  specifies the random seed used to select arguments and actions,
  so runs are reproducible.  Whenever this script is executed, the
  same traces are generated.

- *test_populations*: a test script that uses the Python standard
  library *unittest* module, instead of our own *trun* module. The
  command to run this test is: *python test_populations.py*

There is no stepper in this sample.


Revised Apr 2013
