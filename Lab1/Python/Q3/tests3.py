import unittest  # Import the unittest module
from app2 import RE  # Import the RE class from the code module

class TestPhoneNumberValidation(unittest.TestCase):
    #6. Final Revised tests
    
    def test_valid_phone_number_with_spaces(self):
        # Test a valid phone number with spaces (revised)
        self.assertTrue(RE.check_phone_number("(123) 456 - 7890"))
        
    def test_valid_phone_number_without_spaces(self):
        # Test a valid phone number without spaces (revised)
        self.assertTrue(RE.check_phone_number("(123)123-1234"))
        
    def test_invalid_phone_number(self):
        # Test an invalid phone number
        self.assertFalse(RE.check_phone_number("123123-1234"))
    pass
if __name__ == "__main__":
    unittest.main()  # Run the test cases
