"""
StateCoverage: choose the (aname, args) whose next state has been used least
"""

import sys
import random

# Tester state is a bag of states: [ ( state , n of times used ), ... ]
# Implement bag of states as list of pairs, not dictionary with state keys
#  because our states are themselves dictionaries, which are not hashable.

coverage = list()

# Functions for maintaining coverage

def additems(coverage, enabled):
  # coverage(after) is empty if coverage(before) is empty and enabled is empty
  # 'if' prevents dup of keys in coverage(before) but might be dups in enabled
  coverage += [(next, 0) for (a,args,result,next,properties) in enabled 
                 if next not in [ s for (s,n) in coverage] ]

def inbag(coverage, x):
  # False if coverage is empty, but doesn't crash
  return x in [ s for (s,n) in coverage ] 

def count(coverage, x): 
  # always return first occurence, do dups matter?  
  # index [0] fails if list is empty, is that possible?
  return [ n for (xitem,n) in coverage if xitem == x ][0] 

def incr(coverage, x):
  # get index and replace there, always update first index, do dups matter?
  xs = [ s for (s,n) in coverage ]
  i = xs.index(x) # raise ValueError if x not in xs, is that possible?
  coverage[i] = (x, count(coverage, x) + 1)


def select_action(enabled):
    """
    Choose the action + args whose next state has been used the least
    If more than one action has been used that many of times, choose randomly
    """
    # print 'enabled %s, coverage: %s' % (enabled, coverage)
    if not enabled: # empty 
      return (None, None)
    else:
      additems(coverage, enabled)
      # next line fails if enabled is empty - but it isn't, see above
      # count in next line fails if coverage is empty - possible?
      # no, because additems (above) will execute, and enabled is not empty
      least = min([ count(coverage,next) 
                    for (aname,args,result,next,properties) in enabled ]) 
      aleast = [(aname,args,next) 
                for (aname,args,result,next,properties) in enabled 
                if count(coverage, next) == least]
      # next line fails if aleast is empty - is that possible?
      # could be possible if none in enabled results in next state in least
      # BUT that's not possible because least (above) is built using enabled
      (aname,args,next) = random.choice(aleast)
      incr(coverage,next)
      return (aname,args)
