import unittest

from Q2 import *

class TestIsPalindrome(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_even_length_not_palindrome(self):
        self.assertFalse(is_palindrome("abcxba"))

    def test_null_string(self):
        with self.assertRaises(NullPointerException):
            is_palindrome(None)

    def test_single_letter_palindrome(self):
        self.assertTrue(is_palindrome("G"))

    def test_even_length_not_palindrome_2(self):
        self.assertFalse(is_palindrome("ba"))

if __name__ == "__main__":
    # Generate and display CFG
    cfg = create_cfg()
    draw_cfg(cfg)
    
    # Run the test cases for prime path coverage
    print("\nRunning Prime Path Coverage Test Cases:")
    unittest.main(argv=[''], verbosity=2, exit=False)