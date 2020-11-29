# 实现一个装饰器,打印函数运行时的时间戳
import time


def run_time(func):

    def wrapper(*args, **kwargs):

        print(time.time())
        func(*args, **kwargs)

    return wrapper


@run_time
def test():
    pass

test()
