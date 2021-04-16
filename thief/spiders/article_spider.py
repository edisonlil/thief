import json
import pickle

import scrapy
from scrapy.utils.reqser import request_from_dict
from scrapy_rabbitmq_scheduler.spiders import RabbitSpider
from scrapy_splash import SplashRequest

from thief.items.article import Article
from thief.lib.http_kit import random_user_agent
from thief.parser.spider_parser import spider_parser_factory


import umsgpack





class ArticleSpider(RabbitSpider):


    #allowed_domains = "baidu.com"

    name = "article"

    queue_name = "xxx_urls"

    #items_key = "test_item"

    """
    构建爬虫HTTP头部信息
    """
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': random_user_agent()
    }



    def _make_request(self,mframe,hframe,body):

        try:
           url = str(body,"utf-8")
        except Exception:
            request = request_from_dict(pickle.loads(body),self)
            return request
        # data = json.loads(json_data,encoding="utf-8")

        # url = data["url"]
        # project_id = data["project_id"]



        request = SplashRequest(url=url,callback=self.parse,splash_headers=self.headers)
        return request

        pass
    #
    # def start_requests(self):
    #
    #     for url in self.start_urls:
    #         yield SplashRequest(url=url, callback=self.parse, headers= self.headers)
    #     pass




    def parse(self, response):

        print("开始解析")

        #判断数据类型，选择相应的解析器
        # 进行规则解析
        spider_parser = spider_parser_factory(1,response.text)

        print(response.text)

        yield Article()