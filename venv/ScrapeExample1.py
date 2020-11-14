

import requests
r = requests.get('https://www.usclimatedata.com/climate/united-states/us')
print(len(r.text))

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, features="html.parser")
print(soup.title)
print(soup.title.string)

for link in soup.find_all('a'):
    print(link.get('href'))