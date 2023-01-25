from django.contrib.sites import requests
import io
from PIL import Image
import time
import bs4
import os

# This program aint need to install chrome-driver (or anything similar)
'''
# selenium 3 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.common.by import By
'''

# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def get_images_from_google(wd, delay, max_images, keyword):
    def scroll_down(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)

    url = "https://www.google.com/search?q="+keyword+"&tbm=isch"

    wd.get(url)

    image_urls = set()
    skips = 0

    for i in range(0, 7):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)


    while len(image_urls) + skips < max_images:

        try:
            thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")
        except Exception as e:
            print(e)
            break

        for img in thumbnails[len(image_urls) + skips:max_images]:
            try:
                img.click()
                time.sleep(delay)
            except Exception as e:
                print(e)
                break

            try:
                images = wd.find_elements(By.CLASS_NAME, "n3VNCb")
            except Exception as e:
                print(e)
                break


            for image in images:
                if image.get_attribute('src') in image_urls:
                    max_images += 1
                    skips += 1
                    break

                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    image_urls.add(image.get_attribute('src'))
                    print(f"Found {len(image_urls)}")

    return image_urls


def download_image(download_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + file_name

        with open(file_path, "wb") as f:
            image.save(f, "JPEG")

        print("Downloading Success")
    except Exception as e:
        print('FAILED -', e)


#---main---#



keylist = ['Turmeric','Black galingale','Cinnamomum','Sesamum indicum','Camellia sinensis',
           'Stevia','Cabbage','Banana','Ginger','Siamese senna','Bottle gourd']

parts_list = ["root","leaf","fruit","tree","Flower"]

keyword = [str(i)+" "+str(j) for i in keylist for j in parts_list]
print(keyword)


for k in keyword :
    wd = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    print('______________________________________')
    print("Working on: "+str(k))
    click_delay = 3.5
    max_img = 20

    urls = get_images_from_google(wd, click_delay, max_img, k) # webdriver,delay(sec),max_img
    path = "scraped_images/"+k+"/"

    os.mkdir(path)
    for i, url in enumerate(urls):
        download_image("scraped_images/"+k+"/", url, str(i) + ".jpg")
    wd.close()
    print('______________________________________')
