from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

# Set the path to GeckoDriver executable
gecko_driver_path = r"C:\Users\nanda\OneDrive\Desktop\geckodriver-v0.34.0-win32\geckodriver.exe"  # Update with your actual path

# Set Firefox binary location
firefox_binary_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # Update with your Firefox installation path

# Set Firefox options
options = FirefoxOptions()
options.binary_location = firefox_binary_path
options.add_argument("--start-maximized")

# Initialize the WebDriver
service = FirefoxService(executable_path=gecko_driver_path)
driver = webdriver.Firefox(service=service, options=options)

try:
    # Open Amazon India website
    driver.get("https://www.amazon.in/?ref_=nav_custrec_signin")

    # Example: Find the search box and enter a product name
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("laptop")

    # Click on the search button
    search_button = driver.find_element(By.ID, "nav-search-submit-button")
    search_button.click()

    # Wait for some time to let the page load
    time.sleep(2)

    # Example: Get the title of the first product in the search results
    first_product = driver.find_element(By.XPATH, "//div[@data-component-type='s-search-result']//h2/a")
    product_title = first_product.text

    # Print the product title to console
    print("First product title:", product_title)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
