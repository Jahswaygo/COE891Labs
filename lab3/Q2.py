import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Guru99TitleTest(unittest.TestCase):
    # This class inherits from unittest.TestCase, which is a built-in class in the unittest module.
    # It provides various methods to create and run tests.

    @classmethod
    def setUpClass(cls):
        """Setup WebDriver before running tests"""
        # This method is a class method that sets up the WebDriver before any tests are run.
        # It is executed once for the entire class.
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # The above line initializes the Chrome WebDriver using the ChromeDriverManager to handle the driver installation.
        cls.driver.get("http://demo.guru99.com/test/newtours/")
        # The above line navigates the WebDriver to the specified URL.

    def test_title(self):
        """Test to verify the title of the webpage"""
        # This is a test method that will be run by the unittest framework.
        actual_title = self.driver.title
        # The above line retrieves the title of the current webpage.
        print(f"Page Title: {actual_title}")
        # The above line prints the actual title of the webpage.

        expected_title = "Welcome: Mercury Tours"
        # The above line sets the expected title of the webpage.

        # Assertion to verify the title
        self.assertEqual(actual_title, expected_title, f"Error: Title mismatch! Expected: {expected_title}, Got: {actual_title}")
        # The above line asserts that the actual title matches the expected title.
        # If the titles do not match, it will raise an AssertionError with the specified message.
        print("Title matches the expected value!")
        # The above line prints a success message if the titles match.

    @classmethod
    def tearDownClass(cls):
        """Quit WebDriver after all tests"""
        # This method is a class method that quits the WebDriver after all tests are run.
        # It is executed once for the entire class.
        cls.driver.quit()
        # The above line quits the WebDriver, closing all associated windows.

if __name__ == "__main__":
    unittest.main()
    # The above line runs the test case when the script is executed directly.