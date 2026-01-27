"""
    多层装饰器
    多个装饰器的装饰过程：离函数最近的装饰器先装饰，然后外面的装饰器再进行装饰
"""
from math import sqrt

def get_abs(f):
    def inner(x):
        x = abs(x)
        return f(x)
    return inner

# 将字符串转换为整数的装饰器
def get_integer(f):
    def inner(x):
        x = int(x)
        return f(x)
    return inner


@get_integer
@get_abs # 装饰器语法糖 多个装饰器的装饰过程：离函数最近的装饰器先装饰，然后外面的装饰器再进行装饰
def func(x):
    return sqrt(x)

print(func("-4"))

# abs_inner = get_abs(func)
# int_inner = get_integer(abs_inner)
# print(int_inner("-4"))