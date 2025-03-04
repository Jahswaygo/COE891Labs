import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
from dotenv import load_dotenv

class LinkedInLoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Setup WebDriver before running tests """
        load_dotenv()  # Load environment variables from .env file
        # The above line loads environment variables from a .env file.
        chrome_options = Options()
        # The above line creates an instance of Chrome options.
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        # The above line adds an argument to disable automation control features.
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        # The above line sets a custom user-agent string.
        cls.driver = webdriver.Chrome(options=chrome_options)
        # The above line initializes the Chrome WebDriver with the specified options.
        cls.driver.implicitly_wait(10)
        print("Browser opened successfully.")

    def test_linkedin_login(self):
        """ Test to login to LinkedIn and verify the URL after login """
        # This is a test method that will be run by the unittest framework.
        self.driver.get("https://www.linkedin.com/login")
        # The above line navigates the WebDriver to the LinkedIn login page.
        print("LinkedIn login page opened.")

        # Find the username, password fields and login button
        username_field = self.driver.find_element(By.ID, "username")
        # The above line finds the username field on the LinkedIn login page by its ID attribute.
        password_field = self.driver.find_element(By.ID, "password")
        # The above line finds the password field on the LinkedIn login page by its ID attribute.
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        # The above line finds the login button on the LinkedIn login page by its XPath.

        # Fill in the username and password from environment variables
        username_field.send_keys(os.getenv("MY_LK_USER"))
        # The above line enters the username from the environment variable into the username field.
        password_field.send_keys(os.getenv("MY_LK_PASS"))
        # The above line enters the password from the environment variable into the password field.
        login_button.click()
        # The above line clicks the login button to submit the login form.
        print("Login form submitted.")

        # Wait for the page to load
        time.sleep(20)
        # The above line waits for 20 seconds to allow the page to load.

        # Verify the URL after login
        expected_url = "https://www.linkedin.com/feed/"
        # The above line sets the expected URL after a successful login.
        actual_url = self.driver.current_url
        # The above line retrieves the current URL of the webpage.
        print(f"Actual URL: {actual_url}")
        # The above line prints the actual URL of the webpage.
        self.assertEqual(expected_url, actual_url, "Login failed: URL does not match expected URL.")
        # The above line asserts that the actual URL matches the expected URL.
        # If the URLs do not match, it will raise an AssertionError with the specified message.
        print("Login successful: URL matches expected URL.")

    @classmethod
    def tearDownClass(cls):
        """ Close the WebDriver after tests """
        # This method is a class method that quits the WebDriver after all tests are run.
        # It is executed once for the entire class.
        cls.driver.quit()
        # The above line quits the WebDriver, closing all associated windows.
        print("Browser closed.")

if __name__ == "__main__":
    unittest.main()
    # The above line runs the test case when the script is executed directly.