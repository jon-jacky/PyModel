"""
PyModel configuration -- functions in domains
"""

import random
import populations

# functions that return domains, each function must return a collection

def random9():
    return [ random.randint(0,9) ] # returns singleton list

def current_population():
    return populations.population

# each domain must be a collection, or a callable that returns a collection

populations.domains = { populations.add: { 'ident': 
                                           lambda: [random.randint(0,9)] },
                        # populations.remove: { 'ident': current_population }}
                        populations.remove: { 'ident': populations.population}}

# DEBUG
print 'domainsx, populations.population: id %s, value %s' % \
    (populations.population, id(populations.population))
print 'domainsx, remove["ident"]: id %s, value %s' % \
    (id(populations.domains[populations.remove]['ident']), 
     populations.domains[populations.remove]['ident'])

# for remove, try just using the state variable itself, not the function
# this does NOT work, only first item ever addeded appears in domain.
# that is, the value of the domain is assigned only once when first used.

