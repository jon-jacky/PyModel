"""
PowerSwitch, based on C# example at nmodel.codeplex.com, model program page
"""

### Model

# State

power = False

# Actions

def PowerOn():
  global power
  power = True

def PowerOnEnabled():
  return not power

def PowerOff():
  global power
  power = False

def PowerOffEnabled():
  return power

def Accepting():
  return not power

### Metadata

state = ('power',)

actions = (PowerOn, PowerOff)
enablers = { PowerOn:(PowerOnEnabled,), PowerOff:(PowerOffEnabled,) }
cleanup = (PowerOff,)

# needed for multiple test runs in one session

def Reset(): 
  global power
  power = False
