import configparser

config = configparser.ConfigParser()
config.read("./thief.ini", encoding="utf-8")

"""
"""
def sections():
    global config
    return config.sections()

"""
"""
def options(section):
    global config
    return config.options(section)

"""
"""
def get(option,key):
    global config
    return config.get(option,key)


def getRabbitMqConfig(key):
    global config
    return config.get("rabbitmq",key)