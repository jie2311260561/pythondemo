import os
from urllib.request import urlretrieve
import requests
os.makedirs('./img/',exist_ok=True) #新建文件夹

IMAGE_URL = "https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"
#使用url 下载图片
# urlretrieve(IMAGE_URL,'./img/image1.png')

#使用requests
# 下面的代码实现了和上面一样的功能, 但是稍微长了点. 但我们为什么要提到 requests 的下载呢? 因为使用它的另一种方法, 我们可以更加有效率的下载大文件
#  requests 能让你下一点, 保存一点
r = requests.get(IMAGE_URL,stream =True)
# with open('./img/image2.png','wb') as f:
#     f.write(r.content)
with open('./img/image3.png','wb') as f:
    for chunk in r.iter_content(chunk_size = 32):
        f.write(chunk)