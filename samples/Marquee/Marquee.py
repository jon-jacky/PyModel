"""
Marquee display, pattern crawls from left to right
"""

### Model

# State

display = '* '*13  # short pattern, few states

# Actions, no enabling conditions so always enabled

# Load pattern into display

def Load(pattern):
    global display
    display = pattern

# Then, just shift the pattern to the left, 
# wrapping around from the begining back to end

def Shift():
    global display
    display = display[1:] + display[0]

### Metadata

state = ('display',)

actions = (Shift,)  # but not Load, just keep shifting initial pattern
