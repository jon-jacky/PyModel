
# pmt.py -n 10 -c 3 -s 3 -r 3 WebModel -o WebModelTest_n10_c3_s3_r3

# actions here are just labels, but must be symbols with __name__ attribute

def Initialize(): pass
def ReadInt(): pass
def Login(): pass
def Logout(): pass
def UpdateInt(): pass

# action symbols
actions = (Initialize, ReadInt, Login, Logout, UpdateInt)

testSuite = [
  [
    (Initialize, ()),
    (Logout, ('OleBrumm',)),
    (UpdateInt, ('OleBrumm', 1)),
    (UpdateInt, ('OleBrumm', 1)),
    (UpdateInt, ('OleBrumm', 2)),
    (UpdateInt, ('OleBrumm', 1)),
    (Logout, ('OleBrumm',)),
    (Logout, ('VinniPuhh',)),
  ],
#
  [
    (Initialize, ()),
    (UpdateInt, ('OleBrumm', 1)),
    (UpdateInt, ('OleBrumm', 2)),
    (Logout, ('OleBrumm',)),
    (UpdateInt, ('OleBrumm', 1)),
    (Logout, ('OleBrumm',)),
  ],
#
  [
    (Initialize, ()),
    (UpdateInt, ('VinniPuhh', 1)),
    (UpdateInt, ('VinniPuhh', 1)),
    (UpdateInt, ('VinniPuhh', 2)),
    (Logout, ('VinniPuhh',)),
  ],
]