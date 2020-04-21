from bs4 import BeautifulSoup
from urllib.request import urlopen

html=urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')

#soup=BeautifulSoup(html,features = 'lxml')
soup = BeautifulSoup(html, features='html.parser')
#print('\n',soup.h1)
print(html)
all_href = soup.find_all('a')
all_href = [l['href'] for l in all_href]

print('\n',all_href)