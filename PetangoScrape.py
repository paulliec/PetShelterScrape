#import libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import numpy as np
#BaseUrl = "https://petango.com/pet_search_results?speciesId=1&breedId=undefined&location=45247&distance=50"
#pages = ("", "#page-4")

#go to main page and cycle through search pages, pulling out individual pet urls, save as a list
global pet_links
pet_links = []
for i in range(1, 23):
    page = "https://www.petango.com/pet_search_results?speciesId=1&breedId=undefined&location=45247&distance=50&gender=&size=&age=undefined&color=&goodWithDogs=&goodWithCats=&goodWithChildren=&mustHavePhoto=&mustHaveVideo=&declawed=&animalId=undefined" "#page-" + format(i)
    print(page)
    driver = webdriver.Chrome(executable_path='/Users/paulcarson/Downloads/chromedriver')
    driver.implicitly_wait(30)
    driver.get(page)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    SearchPage = soup.select_one("[class ='page-link']").text

    base_url = 'https://www.petango.com'

    for link in soup.find_all('a'):
        url = link.get('href')
        if url and '/Adopt/Dog' in url:
            pet_links.append(url)
    print(len(pet_links))

    driver.close()



