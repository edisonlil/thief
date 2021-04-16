# Scrapy settings for xxqg project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

#项目名称
BOT_NAME = 'thief'

#Scrapy将在其中寻找spiders的模块列表。
SPIDER_MODULES = ['thief.spiders']

#使用genspider命令在何处创建新spiders的模块。
NEWSPIDER_MODULE = 'thief.spiders'

#供稿使用的编码。
FEED_EXPORT_ENCODING = 'UTF-8'


"""
包含您的项目中启用的下载器中间件。
下载器中间件:优先级(值越高优先级越低)
"""
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    # 指定下载器中间件, 确认任务是否成功
    'scrapy_rabbitmq_scheduler.middleware.RabbitMQMiddleware': 999,
}

"""
包含您的项目中启用的SPIDER中间件
SPIDER中间件:优先级(值越高优先级越低)
"""
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

SPLASH_URL = 'http://115.159.157.148:8050/'
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'


"""
定义管道
管道:优先级(值越高优先级越低)   
"""
ITEM_PIPELINES = {
    "thief.pipelines.acticle_pipeline.ActiclePipeline":300
    # 指定item处理方式, item会加入到rabbitmq中
    #'scrapy_rabbitmq_scheduler.pipelines.RabbitmqPipeline': 300,
}

"""
如果启用，Scrapy将遵守robots.txt策略
默认： False
"""
ROBOTSTXT_OBEY = False

"""
是否启用HTTP缓存。
"""
HTTPCACHE_ENABLED = True

"""
缓存的请求的过期时间（以秒为单位）。
早于此时间的缓存请求将被重新下载。如果为零，则缓存的请求将永不过期。
默认： 0
"""
HTTPCACHE_EXPIRATION_SECS = 0

"""
用于存储（低级）HTTP缓存的目录。如果为空，则将禁用HTTP缓存。如果给出了相对路径，则采用相对于项目数据目录的路径。
默认： 'httpcache'
"""
HTTPCACHE_DIR = "httpcache"

"""
不要使用这些HTTP代码缓存响应。
"""
HTTPCACHE_IGNORE_HTTP_CODES = [404,500]

"""
实现缓存存储后端的类。
默认： 'scrapy.extensions.httpcache.FilesystemCacheStorage'
"""
HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"


# 指定项目的调度器
SCHEDULER = "scrapy_rabbitmq_scheduler.scheduler.SaaS"

# 指定rabbitmq的连接DSN
RABBITMQ_CONNECTION_PARAMETERS = 'amqp://root:123@115.159.157.148:5672/'


# 指定重试的http状态码(重新加回队列重试)
# 如果结果的状态码位该list其中一个则会重试
# SCHEDULER_REQUEUE_ON_STATUS = [500]
