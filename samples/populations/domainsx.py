"""
PyModel configuration -- state-dependendent domain -- show how NOT to do it
"""

import random
import populations

# each domain must be a collection, or a callable that returns a collection
# domain for remove here does NOT work, should use lambda or functions
# to force re-evaluation each time domain is needed

populations.domains = { populations.add: { 'ident': 
                                           lambda: [random.randint(0,9)] },
                        populations.remove: { 'ident': populations.population}}

