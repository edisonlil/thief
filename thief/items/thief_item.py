import scrapy


class ThiefItem(scrapy.Item):

    url = scrapy.Field()

    """
        title = [rule]
    """
    meta = scrapy.Field()

    pass