import scrapy
from scrapy import Request

from scrapy_splash import SplashRequest

from thief.items.article import Article
from thief.lib.http_kit import random_user_agent
from thief.parser.spider_parser import spider_parser_factory

"""
构建爬虫HTTP头部信息
"""
def build_http_header():
    return {
        'Connection': 'keep-alive',
        'User-Agent': random_user_agent()
    }

"""

"""
class ArticleSpider(scrapy.Spider):

    """

    """
    #allowed_domains = "baidu.com"
    """

    """
    name = "article"

    start_urls = ["http://www.baidu.com"]
    """
    
    
    
    # """
    # @property
    # def start_requests(self):
    #
    #     for url in self.start_urls:
    #         yield SplashRequest(url=url, callback=self.parse, headers= build_http_header())
    #     pass

    def start_requests(self):
        yield Request("http://www.baidu.com",meta={"type":1})

    """

    """
    def parse(self, response):




        #判断数据类型，选择相应的解析器
        spider_parser = spider_parser_factory(1,response.text)

        rule = "/html"
        title = spider_parser.parse_rule(rule)
        print(title)
        #进行规则解析

        #



        yield Article()