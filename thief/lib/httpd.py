from fake_useragent import UserAgent

us = UserAgent()
def random_user_agent():
    """
    随机 User-Agent
    :return:
    """
    return us.random
