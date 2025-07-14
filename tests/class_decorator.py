"""
功能简述：研究一下装饰器,逐步看看过程中的结果,好多细节我都没搞清楚
1.
2.

@File           : class_decorator.py
@Author         : Elson.L
@Created        : 2025-07-10
@Last Modified  : 2025-07-10
@Version        :
"""


def decorator(func):
    print("I'm in decorator~")

    def wrapper(*args, **kwargs):
        print("decorator: New function is called")
        result = func(*args, **kwargs)
        print("decorator: Function execution completed")
        print(result)
        return result

    return wrapper


@decorator
def add_num(a: str, b: str) -> str:
    print("add_num: Adding numbers")
    return a + b


add_num("Hello, ", "World!")  # 调用装饰器函数
