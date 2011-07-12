# Like TestIntSuccess but here ReadInt returns wrong value

from WebModel import Initialize, Login, UpdateInt, ReadInt, Logout

testSuite = [
  [
    (Initialize, (), None),
    (Login, ( 'VinniPuhh', 'Correct' ), 'Success'),
    (UpdateInt, ( 'VinniPuhh', 1 ), None),
    (ReadInt, ( 'VinniPuhh', ), 2),  # WRONG! should be 1
    (Logout, ( 'VinniPuhh', ), None)
  ]
]
