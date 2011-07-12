"""
WebApplication offline test generation
"""

cases = [
    ('Generate a test suite with three runs',
     'pmt.py -n 10 -c 3 -s 3 -r 3 WebModel -o WebModelTest_n10_c3_s3_r3'),

    ('Show the generated test suite',
     'type WebModelTest_n10_c3_s3_r3.py')
]
