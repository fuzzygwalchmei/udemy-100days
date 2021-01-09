import re
from bs4 import BeautifulSoup
import lxml
import requests

# with open('website.html') as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'lxml')

# p = soup.find_all(name='p')

# print(soup.find(class_="heading").text)
# print(p)

# print(soup.select_one(selector='p a')) #selector uses css element naming convention


url = "https://news.ycombinator.com/news"

resp = requests.get(url=url)
req = resp.text
soup = BeautifulSoup(req, 'lxml')

# Get all articles and number of votes

articles = soup.select(selector=".storylink")

text = []
links = []

for article in articles:
    text.append(article.getText())
    links.append(article.get("href"))

votes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_='score')]

# Find highest votes article

ind = votes.index(max(votes))

print(f"{text[ind]}: {links[ind]} : {votes[ind]}")