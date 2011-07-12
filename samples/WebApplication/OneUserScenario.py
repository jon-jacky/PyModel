"One user repeatedly logs in, logs out.  Allow interleaving with other actions"

from WebModel import Login, Logout

actions = (Login, Logout) # just these to allow interleaving

initial = 0
accepting = (0,)

graph = ((0, (Login, ( 'VinniPuhh', 'Correct' ), 'Success'), 1),
         (1, (Logout, ( 'VinniPuhh', ), None), 0))

