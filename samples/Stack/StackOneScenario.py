"Restrict Push, Pop to argument 1"

from Stack import Push, Pop

initial = 0
accepting = (0,)

graph = ((0, (Push, (1,), None), 0),
         (0, (Pop, (1,), None), 0))
