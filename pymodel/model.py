"""
Base class for models: ModelProgram, FSM, and TestSuite

The purpose of this class is factor out the code in __init__ and
make_actions that is the same for all models classes.  Each should
call Model.__init__(...) as the first statement in its own __init__
"""

class Model(object):

  def __init__(self, module, exclude, include):
    """
    initializations common to all derived classes
    """
    self.module = module
    self.exclude = exclude
    self.include = include


  def revise_actions(self):
    """
    Revise lists of actions and cleanups accounting for -e --exclude -a --add
    Alter the copies, results might differ from self.module.actions.
    This must be separate from __init__, call after all modules imported
     to account for all pymodel config modules 
    Recall that self.actions can include shared but unused actions
    """
    if self.exclude:
      self.actions = [ a for a in self.actions if a.__name__ not in self.exclude ]
    if self.include:
      self.actions = [ a for a in self.actions if a.__name__ in self.include ]
    if self.exclude:
      self.cleanup = [ c for c in self.cleanup if c.__name__ not in self.exclude ]
    if self.include:
      self.cleanup = [ c for c in self.cleanup if c.__name__ in self.include ]


  def post_init(self):
    """
    This method is called by ProductModelProgram __init__ 
     after all the model modules have been imported
     and all the model objects' __init__ methods have been executed.
    If you override this method in a subclass, make sure the overriding method
     calls Model.post_init() to ensure that revise_actions() is called.
    """
    # Do all of this work here rather than in __init__
    #  so it can include the effects of any pymodel config modules

    # make sure unassigned optional attributes exist
    if not hasattr(self.module, 'cleanup'):
      self.module.cleanup = tuple() # else just use the ones already there
    if not hasattr(self.module, 'observables'):
      self.module.observables = tuple() # no observable actions

    # make copies of collections that may be altered by revise_actions below
    self.cleanup = list(self.module.cleanup) # this works for each class

    # make self.actions differently in each class before calling this post_init
    self.revise_actions()
