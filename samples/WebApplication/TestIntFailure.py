# offline test for WebApplication

from WebModel import *  # Get the action symbols

testSuite = [
  [
    (Initialize, (), None),
    (Login, ( 'VinniPuhh', 'Correct' ), 'Success'),
    (UpdateInt, ( 'VinniPuhh', 1 ), None),
    (Logout, ( 'VinniPuhh', ), None),
    (Login, ( 'VinniPuhh', 'Correct' ), 'Success'),
    (ReadInt, ( 'VinniPuhh', ), 1),
  ]
]
