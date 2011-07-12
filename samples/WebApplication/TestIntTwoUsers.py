
# offline test for WebApplication

from WebModel import *  # Get the action symbols

testSuite = [
  [
    (Initialize, (), None),
    (Login, ( 'VinniPuhh', 'Correct' ), 'Success'),
    (UpdateInt, ( 'VinniPuhh', 1 ), None),
    (Login, ( 'OleBrumm', 'Correct' ), 'Success'),
    (UpdateInt, ( 'OleBrumm', 2 ), None),
    (ReadInt, ( 'OleBrumm', ), 2),
    (ReadInt, ( 'VinniPuhh', ), 1),
    (Logout, ( 'OleBrumm', ), None),
    (Logout, ( 'VinniPuhh', ), None),
    (Login, ( 'OleBrumm', 'Correct' ), 'Success'),
    (Login, ( 'VinniPuhh', 'Correct' ), 'Success'),
    (ReadInt, ( 'VinniPuhh', ), 1),
    (ReadInt, ( 'OleBrumm', ), 2),
    (Logout, ( 'VinniPuhh', ), None),
    (Logout, ( 'OleBrumm', ), None),
  ]
]
