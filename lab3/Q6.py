import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor

class ParallelTest(unittest.TestCase):
    # This class inherits from unittest.TestCase, which is a built-in class in the unittest module.
    # It provides various methods to create and run tests.

    def setUp(self):
        pass  # No setup needed here, WebDriver will be initialized in each test method

    def executSessionOne(self):
        """Test method to execute the first session"""
        chrome_options = Options()
        # The above line creates an instance of Chrome options.
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        # The above line adds an argument to disable automation control features.
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        # The above line sets a custom user-agent string.
        driver = webdriver.Chrome(options=chrome_options)
        # The above line initializes the Chrome WebDriver with the specified options.
        driver.implicitly_wait(10)
        
        
        driver.get("http://demo.guru99.com/V4/")
        # The above line navigates the WebDriver to the specified URL.
        user_id = driver.find_element(By.NAME, "uid")
        # The above line finds the user ID field on the webpage by its name attribute.
        user_id.send_keys("Driver 1")
        # The above line enters the text 'Driver 1' into the user ID field.
        print("Session One executed")
        # The above line prints a message indicating that session one has been executed.
        
        driver.quit()
        # The above line quits the WebDriver, closing all associated windows.

    def executSessionTwo(self):
        """Test method to execute the second session"""
        chrome_options = Options()
        # The above line creates an instance of Chrome options.
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        # The above line adds an argument to disable automation control features.
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        # The above line sets a custom user-agent string.
        driver = webdriver.Chrome(options=chrome_options)
        # The above line initializes the Chrome WebDriver with the specified options.
        driver.implicitly_wait(10)
        
        
        driver.get("http://demo.guru99.com/V4/")
        # The above line navigates the WebDriver to the specified URL.
        user_id = driver.find_element(By.NAME, "uid")
        # The above line finds the user ID field on the webpage by its name attribute.
        user_id.send_keys("Driver 2")
        # The above line enters the text 'Driver 2' into the user ID field.
        print("Session Two executed")
        # The above line prints a message indicating that session two has been executed.
        
        driver.quit()
        # The above line quits the WebDriver, closing all associated windows.

    def executSessionThree(self):
        """Test method to execute the third session"""
        chrome_options = Options()
        # The above line creates an instance of Chrome options.
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        # The above line adds an argument to disable automation control features.
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        # The above line sets a custom user-agent string.
        driver = webdriver.Chrome(options=chrome_options)
        # The above line initializes the Chrome WebDriver with the specified options.
        driver.implicitly_wait(10)
        
        driver.get("http://demo.guru99.com/V4/")
        # The above line navigates the WebDriver to the specified URL.
        user_id = driver.find_element(By.NAME, "uid")
        # The above line finds the user ID field on the webpage by its name attribute.
        user_id.send_keys("Driver 3")
        # The above line enters the text 'Driver 3' into the user ID field.
        print("Session Three executed")
        # The above line prints a message indicating that session three has been executed.
        
        driver.quit()
        # The above line quits the WebDriver, closing all associated windows.

    def tearDown(self):
        pass  # No teardown needed here, WebDriver is closed in each test method

def run_test(test_method):
    """Function to run a test method"""
    suite = unittest.TestSuite()
    # The above line creates a test suite.
    suite.addTest(ParallelTest(test_method))
    # The above line adds the specified test method to the test suite.
    runner = unittest.TextTestRunner()
    # The above line creates a test runner.
    runner.run(suite)
    # The above line runs the test suite using the test runner.

if __name__ == "__main__":
    test_methods = ['executSessionOne', 'executSessionTwo', 'executSessionThree']
    # The above line defines a list of test methods to be run in parallel.
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(run_test, test_methods)
        # The above lines create a thread pool executor with a maximum of 3 workers and map the test methods to be run in parallel.