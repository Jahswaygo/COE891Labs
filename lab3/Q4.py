import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LambdaTestTodoApp(unittest.TestCase):
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
        cls.driver.get("https://lambdatest.github.io/sample-todo-app/")
        # The above line navigates the WebDriver to the specified URL.

    def test_check_items_and_add_name(self):
        """Test to check 'Second Item' and 'Fourth Item', then add a name and submit"""
        # This is a test method that will be run by the unittest framework.
        driver = self.driver
        
        try:
            # Locate and check 'Second Item'
            second_item = driver.find_element(By.NAME, "li2")
            # The above line finds the 'Second Item' checkbox on the webpage by its name attribute.
            second_item.click()
            # The above line clicks the 'Second Item' checkbox to check it.
            self.assertTrue(second_item.is_selected(), "Second Item is not checked!")
            # The above line asserts that the 'Second Item' checkbox is checked.
            # If it is not checked, it will raise an AssertionError with the specified message.

            # Locate and check 'Fourth Item'
            fourth_item = driver.find_element(By.NAME, "li4")
            # The above line finds the 'Fourth Item' checkbox on the webpage by its name attribute.
            fourth_item.click()
            # The above line clicks the 'Fourth Item' checkbox to check it.
            self.assertTrue(fourth_item.is_selected(), "Fourth Item is not checked!")
            # The above line asserts that the 'Fourth Item' checkbox is checked.
            # If it is not checked, it will raise an AssertionError with the specified message.

            # Locate text field, clear it, and add a name
            name_field = driver.find_element(By.ID, "sampletodotext")
            # The above line finds the text field on the webpage by its ID attribute.
            name_field.clear()
            # The above line clears any existing text in the text field.
            name_field.send_keys("Jahmil Ally")  # Replace with your own name
            # The above line enters the specified name into the text field.

            # Submit the form
            add_button = driver.find_element(By.ID, "addbutton")
            # The above line finds the 'Add' button on the webpage by its ID attribute.
            add_button.click()
            # The above line clicks the 'Add' button to submit the form.

            # Verify new item is added
            time.sleep(2)  # Allow time for item to appear
            # The above line waits for 2 seconds to allow the new item to appear on the webpage.
            new_item = driver.find_element(By.XPATH, "//span[text()='Jahmil Ally']")
            # The above line finds the new item on the webpage by its text content.
            self.assertIsNotNone(new_item, "New item was not added!")
            # The above line asserts that the new item is not None.
            # If the new item is not found, it will raise an AssertionError with the specified message.

            # Additional check: Compare actual vs. expected text
            expected_text = "Jahmil Ally"
            # The above line sets the expected text of the new item.
            actual_text = new_item.text
            # The above line retrieves the actual text of the new item.
            self.assertEqual(actual_text, expected_text, "New item text does not match!")
            # The above line asserts that the actual text of the new item matches the expected text.
            # If the texts do not match, it will raise an AssertionError with the specified message.

        except Exception as e:
            print(f"Test failed: {str(e)}")
            # The above line prints the error message if an exception occurs during the test.
            driver.save_screenshot(f"error_screenshot_{int(time.time())}.png")  # Save screenshot for debugging
            # The above line saves a screenshot of the webpage for debugging purposes.
            raise
            # The above line re-raises the exception to indicate test failure.

    @classmethod
    def tearDownClass(cls):
        """Close the WebDriver after tests"""
        # This method is a class method that quits the WebDriver after all tests are run.
        # It is executed once for the entire class.
        cls.driver.quit()
        # The above line quits the WebDriver, closing all associated windows.

if __name__ == "__main__":
    unittest.main()
    # The above line runs the test case when the script is executed directly.
