from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

url = "https://baike.baidu.com/item/%E5%90%B4%E6%81%A9%E8%BE%BE/9465313?fr=aladdin"

html = urlopen(url).read().decode('utf-8')

soup = BeautifulSoup(html,features='lxml') #创建

for item in soup.find_all('div'):
    print(item.get_text())

# text = soup.find_all('div')
# # print(html)


# print(bs.prettify()) # 获取title标签的所有内容
# print(bs.title) # 获取title标签的名称
# print(bs.title.name) # 获取title标签的文本内容
# print(bs.title.string) # 获取head标签的所有内容
# print(bs.head) # 获取第一个div标签中的所有内容
# print(bs.div) # 获取第一个div标签的id的值
# print(bs.div["id"]) # 获取第一个a标签中的所有内容
# print(bs.a) # 获取所有的a标签中的所有内容
# print(bs.find_all("a")) # 获取id="u1"
# print(bs.find(id="u1")) # 获取所有的a标签，并遍历打印a标签中的href的值
# for item in bs.find_all("a"): 
#     print(item.get("href")) # 获取所有的a标签，并遍历打印a标签的文本值
# for item in bs.find_all("a"): 
#     # print(item.get_text())