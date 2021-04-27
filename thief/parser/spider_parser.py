
from thief.type.spider_type import SpiderType

"""
    定义爬虫解析器工厂, 后续可改为注册器模式
"""
def spider_parser_factory(spider_type,text):

    if SpiderType(spider_type) == SpiderType.html:
        return HtmlSpiderParser(text)
    elif SpiderType(spider_type) == SpiderType.json:
        return JSONSpiderParser(text)

    pass


"""
爬虫抽象解析器
"""
class SpiderParser:

    """
    解析的文本内容
    """
    text = None

    def __init__(self,text):
        self.text = text
        pass



    """
        根据规则解析文本
        return str
    """
    def parse_rule(self,rule):
        pass

    pass



from lxml import etree

"""
Html 爬虫解析器
"""
class HtmlSpiderParser(SpiderParser):


    def __init__(self,text):
        SpiderParser.__init__(self,etree.HTML(text))
        pass

    """
        内部调用xpath()
    """
    def parse_rule(self,rule):
        return self.text.xpath(rule)

    pass


import json
"""
JSON 解析库
"""
class JSONSpiderParser(SpiderParser):


    def __init__(self,text):
        SpiderParser.__init__(self,json.loads(text))
        pass

    """
        获取key值
    """
    def parse_rule(self,rule):

        if len(rule) == 0:
            return self.text

        keys = rule.split(".")
        resule = self.text

        for key in keys:
            resule = resule[key]

        return resule
    pass