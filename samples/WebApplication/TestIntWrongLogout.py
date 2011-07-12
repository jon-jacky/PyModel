# Like TestIntSuccess but here ReadInt returns wrong value

from WebModel import Initialize, Login, UpdateInt, ReadInt, Logout

testSuite = [
  [
    (Initialize, (), None),
    (Login, ( 'VinniPuhh', 'Correct' ), 'Success'),
    (UpdateInt, ( 'VinniPuhh', 1 ), None),
    (ReadInt, ( 'VinniPuhh', ), 1),
    (Logout, ( 'OleBrumm', ), None) # WRONG! Should be 'VinniPuhh'
  ]
]
