from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
#导入网页
# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode('utf-8')

soup = BeautifulSoup(html,features='lxml')  
# 匹配图片
# img_links = soup.find_all('img',{"src":re.compile('.*?\.jpg')})  # .匹配除换行符之外的任何单字符 
#                                                                  # *匹配前面的子表达式0次或多次 
#                                                                  # ?匹配前面的子表达式0次或一次 
#                                                                  # \.jpg  ->  .jpg
# for link in img_links:
#     print(link["src"])
#     print(link)

# 匹配学习视频
course_links = soup.find_all('a',{"href":re.compile('https://morvan.*')})
for link in course_links:
    print(link["href"])
