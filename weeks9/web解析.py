# import request
# import scrapy  #优秀的网络爬虫框架
# import pyspider # 专业的网络爬虫技术支持


# import BeautifulSoup #将html解析
# import re #定义和解析 正则表达式 提取web信息  自带
# import python-Goose #提取文章视频元素
# r = request.get('https://api.hithub.com/user',auth = ('user','pass'))

# r.status_code
# r.headers['content-type']
# r.encoding
# r.text
# from goose import Goose  爬取特定功能  文章 视频等


# url = "http://www.elmundo.es/elmundo/2012/10/28/espana/1351388909.html"
# g = Goose({'use_meta_language':False,'target_language':'es'})
# article = g.extract(url = url)
# article.cleaned_text[:150]