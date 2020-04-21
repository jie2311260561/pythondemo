from bs4 import BeautifulSoup
import requests
import os
os.makedirs('./img/',exist_ok=True) #新建文件夹
URL = "http://www.nationalgeographic.com.cn/animals/"
#找到带有img_list的这种ul
html = requests.get(URL).text
soup = BeautifulSoup(html,'lxml')
img_ul = soup.find_all('ul',{"class":"img_list"})
#然后从ul中找到所有的 img 提取 img的src属性 就是图片的网址 然后 使用 requests 一段一段下载
for ul in img_ul:
    imgs =ul.find_all("img")
    for img in imgs:
        url = img["src"]
        r = requests.get(url,stream = True)
        image_name = url.split("/")[-1]
        with open('./img/%s'%image_name,"wb") as t:
            for chunk in r.iter_content(chunk_size=128):
                t.write(chunk)
        print("Save %s"%image_name)
