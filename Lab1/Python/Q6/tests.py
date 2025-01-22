import unittest  
from parameterized import parameterized  # Import the parameterized decorator
from app import PrimeNumberChecker  # Import the PrimeNumberChecker class

class TestPrimeNumberChecker(unittest.TestCase):
    @parameterized.expand([
        (2, True),  # Test case: 2 is a prime number
        (6, False),  # Test case: 6 is not a prime number
        (19, True),  # Test case: 19 is a prime number
        (22, False),  # Test case: 22 is not a prime number
        (23, True),  # Test case: 23 is a prime number
    ])
    def test_is_prime(self, n, expected):
        # Check if the result of is_prime matches the expected value
        self.assertEqual(PrimeNumberChecker.is_prime(n), expected)

if __name__ == "__main__":
    unittest.main()  # Run the test cases
