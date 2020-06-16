from bs4 import BeautifulSoup
import requests

# request the page and assign it to htmlPage variable
htmlPage = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
# parsing the page
psObject = BeautifulSoup(htmlPage.content, "html.parser")
print("Tittle of the page is:", psObject.title.string)
print("links in", psObject.title.string, ": ")

linkList = []
# making a list of all links
for link in psObject('a'):
    linkList.append(link.get('href'))
print(linkList)

# writing the list into a file
with open("linkList.txt", 'w') as f:
    for link in linkList:
        f.write('%s\n' % link)