"""
Stack, based on C# example on TAW'09 slides
"""

### Model

# State

stack = list()
  
# Actions

def Push(x):
  global stack
  stack.insert(0,x)

# Push is always enabled

def Pop(x):
  global stack
  del stack[0]

def PopEnabled(x):
  return (stack and stack[0] == x)

### Metadata

state = ('stack',)

actions = (Push, Pop)

enablers = { Pop:(PopEnabled,) }

domains = { Push: {'x':[1,2]}, Pop: {'x':[1,2]} }

# needed for multiple test runs

def Reset(): 
  global stack
  del stack[:]
