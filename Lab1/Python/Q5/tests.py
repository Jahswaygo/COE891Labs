import unittest  # Import the unittest module
from parameterized import parameterized  # Import the parameterized decorator
from app import Fibonacci  # Import the Fibonacci class

class TestFibonacci(unittest.TestCase):
    @parameterized.expand([
        (0, 0),  # Test case: Fibonacci(0) should be 0
        (1, 1),  # Test case: Fibonacci(1) should be 1
        (2, 1),  # Test case: Fibonacci(2) should be 1
        (3, 2),  # Test case: Fibonacci(3) should be 2
        (4, 3),  # Test case: Fibonacci(4) should be 3
        (5, 5),  # Test case: Fibonacci(5) should be 5
        (6, 8),  # Test case: Fibonacci(6) should be 8
        (7, 13),  # Test case: Fibonacci(7) should be 13
        (8, 21),  # Test case: Fibonacci(8) should be 21
        (9, 34),  # Test case: Fibonacci(9) should be 34
    ])
    def test_compute(self, n, expected):
        # Check if the result of compute matches the expected value
        self.assertEqual(Fibonacci.compute(n), expected)

if __name__ == "__main__":
    unittest.main()  # Run the test cases
