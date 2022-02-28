import requests, lxml
from bs4 import BeautifulSoup
import numpy as np

# params = {
#     "q": 'subject%3A"apprentissage"%20or%20subject%3A"Apprentissage%20par%20problèmes"%20or%20subject%3A"Mémorisation"%20and%20subject%3A"Étudiants"%20and%20subject%3A"stratégie"%20or%20subject%3A"Gamification"',
#     "replies": 20,
# }
#
# url = "https://api.isidore.science/resource/search"
#
# response = requests.get(url, params=params)
# print("réponse : "+str(response))
# if response.ok:
#     soup = BeautifulSoup(response.text, "lxml")
#     with open("soupTest.xml", "w", encoding="utf-8") as f:
#         f.write(str(soup))

f = open("soup.xml", "r", encoding="utf-8")
lines = f.readlines()

rawTitles = []
rawUrls = []

i = 0
prevLine = ""
for line in lines:
    if "<url>" in line:
        rawTitles.append(prevLine)
        rawUrls.append(line)
        print(prevLine)
    prevLine = line

# print(rawTitles)
# print(len(rawTitles))
# print(rawUrls)
# print(len(rawUrls))

titles = [title.replace('<title>', '').replace('</title>\n', '').replace(',', '')
              .replace('<title xml:lang="fr">', '').replace('<title xml:lang="en">', '')
              .replace('<title xml:lang="es">', '') for title in rawTitles]
# print(titles)

urls = [url.replace('<url>', '').replace('</url>\n', '') for url in rawUrls]
# print(urls)

data = []
i = 0
while i < len(titles):
    data.append([titles[i], urls[i]])
    i += 1

# print("data : ")
# print(data)

with open("result.csv", "w", encoding="utf-8") as f:
    for d in data:
        f.write(d[0]+','+d[1]+'\n')
