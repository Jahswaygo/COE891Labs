import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class FacebookEmailFieldTest(unittest.TestCase):
    # This class inherits from unittest.TestCase, which is a built-in class in the unittest module.
    # It provides various methods to create and run tests.

    @classmethod
    def setUpClass(cls):
        """Setup WebDriver before running tests"""
        # This method is a class method that sets up the WebDriver before any tests are run.
        # It is executed once for the entire class.
        cls.driver = webdriver.Chrome()  # Change to webdriver.Firefox() if using Firefox
        # The above line initializes the Chrome WebDriver. You can change it to Firefox if needed.
        cls.driver.implicitly_wait(10)
        # The above line sets an implicit wait of 10 seconds for the WebDriver. This means the WebDriver will wait up to 10 seconds
        # for elements to appear before throwing an exception.

    def test_get_email_field_tag_name(self):
        """Test to find the email field and retrieve its tag name"""
        # This is a test method that will be run by the unittest framework.
        self.driver.get("http://www.facebook.com")
        # The above line navigates the WebDriver to the specified URL.

        # Locate the email field
        email_field = self.driver.find_element(By.NAME, "email")
        # The above line finds the email field on the webpage by its name attribute.

        # Retrieve and print the tag name
        tag_name = email_field.tag_name
        # The above line retrieves the tag name of the email field element.
        print(f"Tag name of the email field: {tag_name}")
        # The above line prints the tag name of the email field.

        # Verify if the tag name is 'input'
        self.assertEqual(tag_name, "input", "Tag name does not match!")
        # The above line asserts that the tag name of the email field is 'input'.
        # If the tag name does not match, it will raise an AssertionError with the specified message.

    @classmethod
    def tearDownClass(cls):
        """Close the WebDriver after running tests"""
        # This method is a class method that quits the WebDriver after all tests are run.
        # It is executed once for the entire class.
        cls.driver.quit()
        # The above line quits the WebDriver, closing all associated windows.

if __name__ == "__main__":
    unittest.main()
    # The above line runs the test case when the script is executed directly.
