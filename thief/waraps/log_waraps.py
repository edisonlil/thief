import logging


def use_logging(msg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            func()
            logging.warning("Waring: "+ msg)
        return wrapper
    return decorator


@use_logging(msg="警告")
def bar():
    print("i am bar")


bar()