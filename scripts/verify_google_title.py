# Import necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Function to verify Google page title
def verify_google_title():
    try:
        # Setup ChromeDriver using WebDriver Manager
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        # Navigate to google.com
        driver.get('https://www.google.com')

        # Wait for the page to load
        time.sleep(3)

        # Verify the page title contains 'Google'
        assert 'Google' in driver.title, f"Title does not contain 'Google'. Actual title: {driver.title}"
        print('Page title verification successful.')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        # Close the browser
        driver.quit()

# Run the function
if __name__ == '__main__':
    verify_google_title()