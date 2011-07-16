"""
Demonstrate programmable domains and state-dependent domains
"""

import random

### Model

# Parameters

maxn = 6

# State

population = set()

# Actions

def add_enabled(ident):
    return len(population) < maxn

def add(ident):
    population.add(ident)
    return tuple(population) # show in progress messages, must be hashable

# population is random (unpredictable)
# so ident can't be drawn from a predefined domain

def remove_enabled(ident):
    return ident in population

def remove(ident):
    population.remove(ident)
    return tuple(population) # show

### Metadata

state = ('population',)

actions = (add, remove)

enablers = { add:(add_enabled,), remove:(remove_enabled,)}

# domain must be a collection, or a callable that returns a collection
# use lambda to ensure that domain is re-evaluated each time it is needed

domains = { add: { 'ident': (lambda: [ random.randint(0,99) ]) }, # singleton
            remove: { 'ident': (lambda: population) } }

def accepting():
    return not population # empty

# needed for multiple test runs

def reset():
    global population
    population = set()
