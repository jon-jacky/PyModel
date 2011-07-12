"""
Stack, here Pop result is return value, not argument
"""

### Model

# State

stack = list()
  
# Actions

def Push(x):
  global stack
  stack.insert(0,x)

# Push is always enabled

def Pop():
  global stack
  result = stack[0]
  del stack[0]
  return result

def PopEnabled():
  return stack     # not empty

### Metadata

state = ('stack',)

actions = (Push, Pop)

enablers = { Pop:(PopEnabled,) }

domains = { Push: {'x':[1,2]} }

def StateFilter():
  return len(stack) < 4

# needed for multiple test runs

def Reset(): 
  global stack
  del stack[:]
