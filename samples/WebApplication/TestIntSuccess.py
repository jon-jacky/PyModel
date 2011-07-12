# offline test for WebApplication

from WebModel import Initialize, Login, UpdateInt, ReadInt, Logout

testSuite = [
  [
    (Initialize, (), None),
    (Login, ( 'VinniPuhh', 'Correct' ), 'Success'),
    (UpdateInt, ( 'VinniPuhh', 1 ), None),
    (ReadInt, ( 'VinniPuhh', ), 1),
    (Logout, ( 'VinniPuhh', ), None)
  ]
]
