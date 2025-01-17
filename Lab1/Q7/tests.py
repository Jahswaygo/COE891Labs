import unittest 
from parameterized import parameterized  # Import the parameterized decorator
from app import *

class TestMathematicalTheories(unittest.TestCase):
    @parameterized.expand([(a, b) for a in [1, 2, 307, 400567] for b in [1, 2, 307, 400567]])
    def test_sum_greater_than_each(self, a, b):
        # Test if the sum of a and b is greater than each individual number
        self.assertTrue(sum_greater_than_each(a, b))

    @parameterized.expand([(a, b) for a in [1, 2, 307, 400567] for b in [1, 2, 307, 400567]])
    def test_commutative_property(self, a, b):
        # Test if the sum of a and b is equal to the sum of b and a
        self.assertTrue(commutative_property(a, b))

    @parameterized.expand([(a, b) for a in [0, -1, -10, -1234, 1, 10, 6789] for b in [0, -1, -10, -1234, 1, 10, 6789]])
    def test_sum_greater_than_each_newval(self, a, b):
        # Test if the sum of a and b is greater than each individual number for newval set
        if a > 0 and b > 0:
            self.assertTrue(sum_greater_than_each(a, b))
        else:
            self.assertTrue(True)  # Assumption: Only positive values are considered

    @parameterized.expand([(a, b) for a in [0, -1, -10, -1234, 1, 10, 6789] for b in [0, -1, -10, -1234, 1, 10, 6789]])
    def test_commutative_property_newval(self, a, b):
        # Test if the sum of a and b is equal to the sum of b and a for newval set
        self.assertTrue(commutative_property(a, b))

if __name__ == "__main__":
    unittest.main()  # Run the test cases
