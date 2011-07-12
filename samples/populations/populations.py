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

domains = { add: { 'ident': (lambda: [ random.randint(0,99) ]) }, # singleton
            remove: { 'ident': (lambda: population) } }

# remove domain ensures we only try to remove elements that are in the set
# in remove, just using { 'ident' : population } doesn't work here, 
# because population is empty now, when the dictionary is built

def accepting():
    return not population # empty

# needed for multiple test runs

def reset():
    global population
    population = set()
