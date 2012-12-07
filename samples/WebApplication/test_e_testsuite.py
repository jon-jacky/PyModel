"""
Test -e and -a options with TestSuite
"""

cases = [
    ('Test suite with two runs:',
     'pmv TestIntTwoRuns'),

    ('Same test suite with -e Logout',
     'pmv TestIntTwoRuns -e Logout -o TestIntTwoRuns_NoLogout'),

    ('Same test suite with -a Initialize -a Login -a UpdateInt',
     'pmv TestIntTwoRuns -a Initialize -a Login -a UpdateInt -o TestIntTwoRuns_Add'),
]
