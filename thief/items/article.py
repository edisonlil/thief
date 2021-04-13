import scrapy

"""
文章存储信息
@author edison
"""


class Article(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    author = scrapy.Field()
    pass
