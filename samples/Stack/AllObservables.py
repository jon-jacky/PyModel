"""pymodel config"""

import Stack

# Pop should return values from Push in test suite or stepper

Stack.observables = (Stack.Push, Stack.Pop)  
