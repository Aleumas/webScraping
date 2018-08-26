import requests
from bs4 import BeautifulSoup
import pandas


r = requests.get('https://techcrunch.com/')

soup = BeautifulSoup(r.text, "html.parser")

content = soup.find('div', {"class": "content"})

crunchTitles = content.findAll('a', {'class': 'post-block__title__link'})

titles = []

for title in crunchTitles:
    titleName = title.decode_contents()[5:-3]
    titles.append(titleName)

dataFrame = pandas.DataFrame(titles)


print(dataFrame)
