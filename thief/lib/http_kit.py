from fake_useragent import UserAgent

def random_user_agent():
    us = UserAgent()
    return us.random
