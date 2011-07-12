# offline test for WebApplication

from WebModel import *  # Get the action symbols

testSuite = [
  [
    (Initialize, (), None),
    (Login, ( 'OleBrumm', 'Incorrect' ), 'Failure'),
    (Login, ( 'OleBrumm', 'Incorrect' ), 'Failure'),
    (Login, ( 'VinniPuhh', 'Incorrect' ), 'Failure'),
    (Login, ( 'VinniPuhh', 'Incorrect' ), 'Failure'),
    (Login, ( 'VinniPuhh', 'Incorrect' ), 'Failure'),
    (Login, ( 'OleBrumm', 'Correct' ), 'Success')
  ]
]
