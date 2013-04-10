"""
Use the unittest framework to execute the same tests as in test.py, 
Test succeeds in unittest if pmt.py command returns success status to shell
So this test succeeds if pmt runs and does not crash, 
even if pmt reports PyModel test failed.
"""

import unittest
import os

class PopulationTest(unittest.TestCase):

    def test_n6(self):
        """pmt -n 6 populations, no seed so different test run each time"""
        status = os.system('pmt -n 6 populations')
        self.assertEqual(status, 0) # command returned success status to shell

if __name__ == '__main__':
    unittest.main()
