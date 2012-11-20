"""
PyModel configuration - state filter, limit population to 3
"""

import populations

def filter3():
    return len(populations.population) <= 3

populations.statefilter = filter3
