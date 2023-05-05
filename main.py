import requests
from bs4 import BeautifulSoup

url = 'https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html'
html = requests.get(url)
# print(html.text)

s = BeautifulSoup(html.content, 'html.parser')

article_title = s.find('h1',{'class':'headline__text'})
article_content = s.find("div",class_="article__content")
print("title",article_title.text.strip())
print("content",article_content.get_text(' ',strip=True))
