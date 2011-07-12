"""pymodel config"""

import Stack

def StackDepthThree():
    return len(Stack.stack) <= 10

Stack.StateFilter = StackDepthThree
