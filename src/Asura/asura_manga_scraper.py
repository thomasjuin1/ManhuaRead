from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from manga_class import Manga

# Initialize ChromeOptions and set headless mode
chrome_options = Options()
#chrome_options.add_argument('--headless')

# Initialize the web driver with the options
driver = webdriver.Chrome(options=chrome_options)  # Use other drivers similarly

# Navigate to the website
url = "https://asuratoon.com/manga"
driver.get(url)

# Extract and print the titles
MangaList = []
i = 0
post_titles = driver.find_elements(By.CLASS_NAME, "bsx")
for (post) in post_titles:
    a_tag = post.find_element(By.TAG_NAME, "a")
    href_value = a_tag.get_attribute("href")
    print(href_value)

"""
last_page = False
while (last_page == False):
    button = driver.find_elements(By.CLASS_NAME, "r")
    post_titles = driver.find_elements(By.CLASS_NAME, "bsx")
    if (button == []):
        last_page = True
    for post in post_titles:
        print("Post number: "+ str(i))
        MangaList.append(Manga(post.text.split("\n")))
        i = i + 1
    if (last_page == False):
        button[0].click()

MangaList.sort(key=lambda x: x.title)
for manga in MangaList:
    print(manga)
"""
# Close the web driver
driver.quit()