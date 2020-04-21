# import scrapy

# #导入模块后创建一个类 继承 scrapy.spider 还要起一个名字 这里不需要去重 因为scrapy 自动帮你做了

# class GaojieSpider(scrapy.Spider):
#     name = "gaojie"
#     start_urls =  [
#          'https://morvanzhou.github.io/',
#     ]
#     # unseen = set()
#     # seen = set()      # 我们不在需要 set 了, 它自动去重
#     #  我们使用 python 的 yield 来返回搜集到的数据 (为什么是yield? 因为在 scrapy 中也有异步处理, 加速整体效率). 
#     # 这些 title 和 url 的数据, 我们都是用 scrapy 中抓取信息的方式.

#     def parse(self,response):
#         yield{ #return some results
#             'title':response.css("h1::text").extract_first(default = "Missing").strip().replace(","),
#             'url':response.url,
#         }
#         urls = response.css('a::attr(href)').re(r'^/.+?/$')
#         for url in urls:
#             yield response.follow(url,callable = self.parse)
import scrapy


class MofanSpider(scrapy.Spider):
    name = "mofan"
    start_urls = [
        'https://morvanzhou.github.io/',
    ]
    # unseen = set()
    # seen = set()      # we don't need these two as scrapy will deal with them automatically

    def parse(self, response):
        yield {     # return some results
            'title': response.css('h1::text').extract_first(default='Missing').strip().replace('"', ""),
            'url': response.url,
        }

        urls = response.css('a::attr(href)').re(r'^/.+?/$')     # find all sub urls
        for url in urls:
            yield response.follow(url, callback=self.parse)     # it will filter duplication automatically
