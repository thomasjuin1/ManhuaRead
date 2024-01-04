from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from src.Api.models.manga import Manga, MangaDb, MangaUserDb
from src.Api.database.pymongo_manga import insert_manga, update_manga
from chromedriver_py import binary_path
import threading

FinalMangaList = []
Lock = threading.Lock()

def AsuraScraper(headless : bool = True):
    # Initialize ChromeOptions and set headless mode
    chrome_options = Options()
    if (headless == True):
        chrome_options.add_argument('--headless')
        
    # Initialize the web driver with the options
    svc = webdriver.ChromeService(binary_path)
    driver = webdriver.Chrome(service=svc, options=chrome_options)

    # Navigate to the website
    try:
        url = "https://asuratoon.com/"
        driver.get(url)
    except Exception as e:
        print("Error: Unable to connect to the website:", str(e))
        exit(84)

    MangaList = []
    i = 0

    last_page = False
    while (last_page == False):
        button = driver.find_elements(By.CLASS_NAME, "r")
        post_titles = driver.find_elements(By.CLASS_NAME, "uta")
        for post in post_titles:
            MangaList.append(Manga())
            a_tag = post.find_element(By.TAG_NAME, "a")
            href_value = a_tag.get_attribute("href")
            MangaList[i].link = href_value
            i = i + 1
        try:
            break
            button[0].click()
        except:
            print("Error: Unable to click on the button")
            last_page = True
    driver.quit()
    MangaList = AsuraMangaScraper(MangaList)
    for manga in MangaList:
        print(manga.title)
        insert_manga(manga)
    return MangaList

def AsuraMangaScraper(MangaList):

    try:
        i = 0
        max_i = len(MangaList)
        max_threads = 10
        threads = []

        while (i < max_i):
            if (len(threads) < max_threads):
                thread = threading.Thread(target=AsuraThreadScraper, args=(MangaList[i].link,))
                thread.start()
                threads.append(thread)
                i = i + 1
            else:
                for thread in threads:
                    thread.join()
                    threads.remove(thread)

        for thread in threads:
            thread.join()
            threads.remove(thread)
    except Exception as e:
        print("Error: Unable to start the threads:", str(e))
        return FinalMangaList

    # Close the web driver
    return FinalMangaList

def AsuraThreadScraper(url):
    manga : Manga = Manga()

    # Initialize ChromeOptions and set headless mode
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    # Initialize the web driver with the options
    svc = webdriver.ChromeService(binary_path)
    driver = webdriver.Chrome(service=svc, options=chrome_options)

    # Navigate to the website
    try:
        driver.get(url)
    except Exception as e:
        print("Error: Unable to connect to the website:", str(e))
        exit(84)

    manga.link = url

    #   Image box
    try:
        imageBox = driver.find_element(By.CLASS_NAME, "thumbook")
        #   Image
        image = imageBox.find_element(By.CLASS_NAME, "wp-post-image")
        manga.image = image.get_attribute("src")
    except:
        manga.image = "N/A"

    #   Rating
    try:
        rating_info = driver.find_element(By.CLASS_NAME, "rating")
        note = rating_info.find_element(By.CLASS_NAME, "num")
        manga.note = note.get_attribute("content")
    except:
        manga.note = "N/A"

    #   Type & Status
    try:
        type_status = imageBox.find_element(By.CLASS_NAME, "tsinfo")
        type_status_split = type_status.text.split("\n")
        if (len(type_status_split) == 4):
            manga.status = type_status_split[1]
            manga.type = type_status_split[3]
    except:
        manga.status = "N/A"
        manga.type = "N/A"

    #   Info box
    info_box = driver.find_element(By.CLASS_NAME, "infox")

    #   Title
    try:
        title = info_box.find_element(By.CLASS_NAME, "entry-title")
        manga.title = title.text
    except:
        manga.title = "N/A"

    #   Synopsis
    try:
        synopsis = info_box.find_element(By.CLASS_NAME, "entry-content")
        #   Remove the trailing spaces and trailing lines
        final_synopsis = synopsis.text.rstrip()
        manga.synopsis = final_synopsis
    except:
        manga.synopsis = "N/A"

    #   Genres
    try:
        genres = info_box.find_element(By.CLASS_NAME, "mgen")
        genres = genres.find_elements(By.TAG_NAME, "a")
        manga.genres = []
        for genre in genres:
            manga.genres.append(genre.text)
    except:
        manga.genres = "N/A"

    #   Chapters
    try:
        chapter_list = driver.find_element(By.CLASS_NAME, "eplister")
        #   Get the <li> tag
        chapter_list = chapter_list.find_elements(By.TAG_NAME, "li")
        manga.chapters = str(len(chapter_list))
    except:
        manga.chapters = "N/A"

    driver.quit()
    Lock.acquire()
    FinalMangaList.append(manga)
    Lock.release()
    return manga

#AsuraScraper()