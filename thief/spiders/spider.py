import json
import logging
import pickle

import scrapy
from scrapy.utils.reqser import request_from_dict
from scrapy_rabbitmq_scheduler.spiders import RabbitSpider
from scrapy_splash import SplashRequest

from thief.items.article import Article
from thief.lib.httpd import random_user_agent
from thief.parser.spider_parser import spider_parser_factory
from thief.type.spider_type import SpiderType

logger = logging.getLogger(__name__)

class ThiefSpider(RabbitSpider):

    name = "article"

    queue_name = "xxx"

    """
    构建爬虫HTTP头部信息
    """
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': random_user_agent()
    }

    def create_request(self,item):

        url = item["url"]
        fields = item["fields"]
        type = item["type"]
        if SpiderType(type) == SpiderType.html:
            return SplashRequest(url=url, callback=self.parse, splash_headers=self.headers,
                                     cb_kwargs={"fields": fields, "type": type})
        else:
            return scrapy.Request(url=url, callback=self.parse, headers=self.headers,
                                     cb_kwargs={"fields": fields, "type": type})


    def _make_request(self,mframe,hframe,body):

        """
        选择发起请求策略 simple,splash
        {"url":"https://www.xuexi.cn/lgpage/detail/index.html?id=10522373568484213565&item_id=10522373568484213565","fields":{"content":"/html/body/div[@id='root']/div[@class='main-view']/section[@class='_3GhgGH8Y4Zh8H0uBP5aUMD _3mVsbsHWKWuZwBS5zIrFO9']/div[@class='oSnRgpdW2BnrDruxKh9We _3mVsbsHWKWuZwBS5zIrFO9']/div/div/div[@class='Iuu474S1L6y5p7yalKQbW grid-gr']/div[@class='grid-cell'][2]/section[@class='_3GhgGH8Y4Zh8H0uBP5aUMD _3mVsbsHWKWuZwBS5zIrFO9']/div[@class='oSnRgpdW2BnrDruxKh9We _3mVsbsHWKWuZwBS5zIrFO9']/div/div/div[@class='Iuu474S1L6y5p7yalKQbW grid-gr']/div[@class='grid-cell']/div[@class='render-detail-article']/div[@class='render-detail-article-content']/div[@class='render-detail-content cke-mode']"},"type":1}
        """

        try:
            item = json.loads(str(body, "utf-8"))
        except Exception:
            #request = request_from_dict(pickle.loads(body),self)
            logger.error("请求信息有误,忽略该请求")
            return request_from_dict(pickle.loads(body),self)

        return self.create_request(item)


    #https://gw-proxy-api.xuexi.cn/v1/api/exchangeAuthUrl

    def parse(self, response,**kwargs):

        logger.debug('开始解析 %s 请求',response.url)


        #判断数据类型，选择相应的解析器
        type = self.get_kwargs(kwargs,"type")
        spider_parser = spider_parser_factory(type, response.text)

        # 进行规则解析
        fields = self.get_kwargs(kwargs,"fields")
        for key in fields:
            print(key + ':' + json.dumps(spider_parser.parse_rule(fields[key])))


        yield Article()


    def get_kwargs(self,kwargs,key):
        for k, v in kwargs.items():
            logger.debug('Optional argument %s (kwargs): %s' % (k, v))
            if k == key:
                return v