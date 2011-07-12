""""
One user repeatedly logs in, logs out. 
Suppress interleaving with ReadInt, UpdateInt actions
"""

from WebModel import Login, Logout, UpdateInt, ReadInt

actions = (Login, Logout, UpdateInt, ReadInt) # interleave Initialize only

initial = 0
accepting = (0,)

graph = ((0, (Login, ( 'VinniPuhh', 'Correct' ), 'Success'), 1),
         (1, (Logout, ( 'VinniPuhh', ), None), 0))

