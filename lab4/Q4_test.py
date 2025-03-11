import unittest
from unittest.mock import patch
from io import StringIO
from Q4 import print_primes

class TestPrintPrimes(unittest.TestCase):
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_path_1(self, mock_stdout):
        """
        Test path: 1 -> 2 -> 3 -> 10 -> 11 -> 10 -> 12
        Input: n = 1
        Explanation: This path covers the edges from the start to the initialization,
        checks the while loop condition (which is false), and then moves to the for loop to print the primes.
        """
        expected_output = "Prime: 2\nVisited Nodes: [1, 2, 3, 10, 11, 10, 12]\n"
        print_primes(1)
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output.strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_path_2(self, mock_stdout):
        """
        Test path: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 5 -> 8 -> 9 -> 3 -> 10 -> 11 -> 10 -> 12
        Input: n = 2
        Explanation: This path covers the edges from the start to the initialization,
        checks the while loop condition (which is true), executes the while loop body,
        checks the for loop condition, finds a prime, and then moves to the for loop to print the primes.
        """
        expected_output = "Prime: 2\nPrime: 3\nVisited Nodes: [1, 2, 3, 4, 5, 6, 5, 8, 9, 3, 10, 11, 10, 11, 10, 12]\n"
        print_primes(2)
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()