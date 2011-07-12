"""
ActionNameCoverage: choose the action name which has been used least
"""

import sys
import random

# Tester state is a bag of action names: { aname : n of times used }

coverage = dict()

def SelectAction(enabled):
    """
    Choose the action symbol which has been used the least number of times.
    If more than one action has been used that many times, choose randomly.
    """
    if not enabled: # empty 
      return (None, None)
    else:
      coverage.update(dict([(aname,0) 
                            for (aname,args,result,next,properties) in enabled 
                            if aname not in coverage])) # multiple occurs OK
      least = min([coverage[aname] 
                   for (aname,args,result,next,properties) in enabled]) 
      aleast = [(aname,args) for (aname,args,result,next,properties) in enabled 
                                 if coverage[aname] == least]
      (aname,args) = random.choice(aleast)
      coverage[aname] += 1
      return (aname,args)

