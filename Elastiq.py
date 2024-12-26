import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Elastic:

    def assignment_ai(self):
        # Initialize WebDriver (ensure the correct driver is downloaded and in PATH)
        driver = webdriver.Chrome()

        try:
            # Navigate to the Selenium Playground website
            driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")  # Replace with the actual URL

            # Locate the search box and input the search term "New York"
            search_box = driver.find_element(By.XPATH, "//input[@type='search']")
            search_box.send_keys("New York")  # Input the search term

            # Wait for the results to update dynamically (if necessary)
            time.sleep(2)  # Use explicit waits for a better approach

            # Locate the element that displays the entries information
            entries_info = driver.find_element(By.XPATH, "//div[@id='example_info']")

            # Validate the text directly
            expected_text = "Showing 1 to 5 of 5 entries (filtered from 24 total entries)"
            actual_text = entries_info.text.strip()  # Strip any extra whitespace
            assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"

            print("Validation successful: Entries information matches the expected text.")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            # Quit the driver
            driver.quit()


# Create an instance of the Elastic class and call the assignment_ai method
elastic = Elastic()
elastic.assignment_ai()
