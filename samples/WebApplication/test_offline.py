"""
WebApplication offline test generation
"""

cases = [
    ('Generate a test suite with three runs',
     'pmt -n 10 -c 3 -s 3 -r 3 WebModel -o WebModelTest_n10_c3_s3_r3'),

    ('Show the generated test suite',
     'more WebModelTest_n10_c3_s3_r3.py') # 'more' is the same in Unix and Windows

    # Now you can run the generated test suite:
    #  pmt WebModelTest_n10_c3_s3_r3
    # check the generated test suite agains the model:
    #  pmt WebModelTest_n10_c3_s3_r3 WebModel
    # execute the generated test suite on the web application:
    #  wsgirunner webapp # start the web application on localhost
    #  pmt WebModelTest_n10_c3_s3_r3 -i Stepper
]
