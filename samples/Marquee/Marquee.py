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

# Then, just shift the pattern to the right,
# wrapping around from the end back to the beginning

def Shift():
    global display
    display = display[-1] + display[:-1]

### Metadata

state = ('display',)

actions = (Shift,)  # but not Load, just keep shifting initial pattern
