# Elastiq.AI-assignment
This is elastic assignment repo
Project Title
Selenium Automation Script for Validating Search Functionality on a Webpage

Description
This Python script automates the process of validating the search functionality on a webpage. Specifically, it verifies that entering the term "New York" in the search box displays the expected results information:
"Showing 1 to 5 of 5 entries (filtered from 24 total entries)."

The script uses Selenium WebDriver for browser automation.

Prerequisites
Before running the script, ensure the following are installed and configured on your system:

Python (version 3.7 or above)

Download and install Python from python.org.
Google Chrome Browser

Download and install the latest version of Chrome from google.com/chrome.
ChromeDriver

Download the appropriate ChromeDriver for your browser version from chromedriver.chromium.org.
Selenium Python Library

Install Selenium using pip:
bash
Copy code
pip install selenium
Setup and Usage
1. Clone or Download the Script
Save the script to your local system in a .py file (e.g., elastic_assignment.py).

2. Replace the Placeholder URL
Replace the placeholder URL "https://www.lambdatest.com/selenium-playground/table-sort-search-demo" in the script with the actual URL of the Selenium Playground website.

3. Run the Script
Execute the script using Python:

bash
Copy code
python elastic_assignment.py
4. Expected Output
If the search functionality works as expected, the script will print:
plaintext
Copy code
Validation successful: Entries information matches the expected text.
If there’s an issue, it will print an error message detailing the problem.
Code Explanation
Key Features
Input Search Query:

The script inputs the term "New York" in the search box using its XPath locator.
Dynamic Results Validation:

It locates the results summary (//div[@id='example_info']) and validates it against the expected text.
Error Handling:

The script uses a try-except block to handle any exceptions that occur during execution.
Clean Up:

The WebDriver instance is closed gracefully using driver.quit().
Best Practices Followed
Element Locators: XPath is used to locate elements efficiently.
Assertions: Used to ensure the actual results match the expected output.
Modular Design: Encapsulated functionality in a class for better reusability.
Browser Compatibility: Script designed for Chrome but can be adapted to other browsers.
How to Customize
Search Term: Replace "New York" in the send_keys method with your desired search query.
Expected Text: Update the expected_text variable if the expected output differs.
Browser: To switch to another browser (e.g., Firefox), replace webdriver.Chrome() with webdriver.Firefox() and ensure the corresponding driver is installed.
Troubleshooting
Issue: "Driver not found"
Solution: Ensure ChromeDriver is downloaded and added to your system's PATH.

Issue: "Element not found"
Solution: Verify the XPath or CSS selectors used in the script.

Contact
For questions or issues, feel free to contact:
Email: [ramyaailuri43@gmail.com]
