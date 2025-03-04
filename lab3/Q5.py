import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

class GoogleSearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Setup WebDriver before running tests """
        # This method is a class method that sets up the WebDriver before any tests are run.
        # It is executed once for the entire class.
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

    def test_search_facebook_and_verify_title(self):
        """ Test to search for 'Facebook', click the first result, and verify the page title """
        # This is a test method that will be run by the unittest framework.

        # Step 1: Launch Google
        self.driver.get("http://www.google.com")
        # The above line navigates the WebDriver to the specified URL.
        print("Google launched.")

        # Step 2: Perform search for 'Facebook'
        time.sleep(random.uniform(2, 5))  # Wait for Google to load
        # The above line waits for a random time between 2 to 5 seconds to simulate human behavior.
        search_box = self.driver.find_element(By.NAME, "q")
        # The above line finds the search box on the Google homepage by its name attribute.
        search_box.send_keys("Facebook")
        # The above line enters the search term 'Facebook' into the search box.
        search_box.submit()
        # The above line submits the search form.
        print("Searched for Facebook.")

        # Step 3: Wait for results to load and click the first search result
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h3"))
        )
        # The above lines wait up to 20 seconds for the search results to load and locate the first result by its XPath.
        first_result = self.driver.find_element(By.XPATH, "//h3")
        # The above line finds the first search result on the webpage by its XPath.
        first_result.click()
        # The above line clicks the first search result.
        print("Clicked the first search result.")

        # Step 4: Verify the page title contains 'Facebook'
        time.sleep(random.uniform(15, 25))  # Wait for page to load
        # The above line waits for a random time between 15 to 25 seconds to allow the page to load.
        for _ in range(5):
            actual_title = self.driver.title
            # The above line retrieves the title of the current webpage.
            current_url = self.driver.current_url
            # The above line retrieves the current URL of the webpage.
            print(f"Page Title: {actual_title}")
            # The above line prints the actual title of the webpage.
            print(f"Current URL: {current_url}")
            # The above line prints the current URL of the webpage.
            if "Facebook" in actual_title:
                break
            # The above line breaks the loop if the title contains 'Facebook'.
            time.sleep(5)  # Wait a bit longer if the title is not correct
            # The above line waits for 5 seconds before checking the title again.

        self.assertTrue("Facebook" in actual_title, "Error: Title does not contain 'Facebook'.")
        # The above line asserts that the actual title contains 'Facebook'.
        # If the title does not contain 'Facebook', it will raise an AssertionError with the specified message.
        print("Page title verified.")

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
