"""pymodel config"""

import Stack

def Depth3():
    return len(Stack.stack) < 4

Stack.StateFilter = Depth3
