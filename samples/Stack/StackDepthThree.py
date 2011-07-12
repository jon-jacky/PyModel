"""pymodel config"""

import Stack

def StackDepthThree():
    return len(Stack.stack) <= 3

Stack.StateFilter = StackDepthThree
