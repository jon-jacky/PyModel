"like scenario_login.txt in NModel WebApplication"

from WebModel import Login, Logout

actions = (Login, Logout) # just these to allow interleaving

testSuite = [
  [
    (Login, ( 'VinniPuhh', 'Correct' ), 'Success'),
    (Logout, ( 'VinniPuhh', ), None)
  ]
]


