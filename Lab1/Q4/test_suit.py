import unittest
import sys
import os

# Add the Q2 and Q3 directories to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Q2')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Q3')))

# Import the test cases from the correct modules
from tests import TestTriangle
from tests3 import TestPhoneNumberValidation

# Create a test suite
def suite():
    suite = unittest.TestSuite()
    # Add test cases from Q2/test.py
    suite.addTest(unittest.makeSuite(TestTriangle))
    # Add test cases from Q3/test3.py
    suite.addTest(unittest.makeSuite(TestPhoneNumberValidation))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())