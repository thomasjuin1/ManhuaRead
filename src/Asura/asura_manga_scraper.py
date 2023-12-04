from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from manga_class import Manga

# Initialize ChromeOptions and set headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')

# Initialize the web driver with the options
driver = webdriver.Chrome(options=chrome_options)  # Use other drivers similarly

# Navigate to the website
try:
    url = "https://asuratoon.com/"
    driver.get(url)
except:
    print("Error: Unable to connect to the website")
    exit(84)

# Extract and print the titles
MangaList = []
i = 0

post_titles = driver.find_elements(By.CLASS_NAME, "bsx")
last_page = False
while (last_page == False):
    button = driver.find_elements(By.CLASS_NAME, "r")
    post_titles = driver.find_elements(By.CLASS_NAME, "bsx")
    for post in post_titles:
        print("Post number: "+ str(i))
        print(post.text)
        if (button == []):
            print("Last page")
            last_page = True
        if (button != []):
            print("Page number: "+str(i))
        MangaList.append(Manga(post.text.split("\n")))
        a_tag = post.find_element(By.TAG_NAME, "a")
        href_value = a_tag.get_attribute("href")
        MangaList[i].link = href_value
        i = i + 1
    try:
        button[0].click()
    except:
        print("Error: Unable to click on the button")
        last_page = True

MangaList.sort(key=lambda x: x.title)
for manga in MangaList:
    print(manga)

# Close the web driver
driver.quit()