from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Initialize ChromeOptions and set headless mode
chrome_options = Options()
#chrome_options.add_argument('--headless')

# Initialize the web driver with the options
driver = webdriver.Chrome(options=chrome_options)  # Use other drivers similarly

# Navigate to the website
url = "https://asuratoon.com/"
driver.get(url)

# Find elements with post titles
post_titles = driver.find_elements(By.CLASS_NAME, "bs")

# Extract and print the titles
for post in post_titles:
    print(post.text)

# Close the web driver
driver.quit()