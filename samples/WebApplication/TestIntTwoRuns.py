# offline test for WebApplication

from WebModel import Initialize, Login, UpdateInt, ReadInt, Logout

testSuite = [

  # Run 1 should succeed
  [
    (Initialize, (), None),
    (Login, ( 'VinniPuhh', 'Correct' ), 'Success'),
    (UpdateInt, ( 'VinniPuhh', 1 ), None),
    (ReadInt, ( 'VinniPuhh', ), 1),
    (Logout, ( 'VinniPuhh', ), None)
  ],

  # Run 2 should fail due to error in implementation
  [
    (Initialize, (), None),
    (Login, ( 'VinniPuhh', 'Correct' ), 'Success'),
    (UpdateInt, ( 'VinniPuhh', 1 ), None),
    (Logout, ( 'VinniPuhh', ), None),
    (Login, ( 'VinniPuhh', 'Correct' ), 'Success'),
    (ReadInt, ( 'VinniPuhh', ), 1),
  ]

]
