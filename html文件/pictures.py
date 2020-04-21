from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode('utf-8')
print(html)
soup = BeautifulSoup(html, features='html.parser')

img_links = soup.find_all("img", {"src": re.compile('.*?\.jpg')})#挑选图片的正则表达式
for link in img_links:
    print(link['src'])

course_links = soup.find_all('a', {'href': re.compile('https://morvan.*')})#挑选课程链接的正则表达式
for link in course_links:
    print(link['href'])