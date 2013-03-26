"""pymodel config"""

import Stack

def StackDepthThree():
    return len(Stack.stack) <= 10  # not 3 -!?

Stack.StateFilter = StackDepthThree
