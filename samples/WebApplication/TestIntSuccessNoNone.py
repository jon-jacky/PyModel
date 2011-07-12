# compare to TestIntSuccess 
# Final None can be omitted from action tuples when there is no return value
# offline test for WebApplication

from WebModel import Initialize, Login, UpdateInt, ReadInt, Logout

testSuite = [
  [
    (Initialize, ()),
    (Login, ( 'VinniPuhh', 'Correct' ), 'Success'),
    (UpdateInt, ( 'VinniPuhh', 1 )),
    (ReadInt, ( 'VinniPuhh', ), 1),
    (Logout, ( 'VinniPuhh', ))
  ]
]
