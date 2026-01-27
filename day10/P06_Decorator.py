"""
    装饰器
    装饰器允许在不修改原有函数代码的基础上，动态地增加或拓展函数的功能。
    装饰器本质上是一个接收函数作为输入并返回一个新的包装过后的函数的对象。
    def decorator(func):
        def inner(参数):
            # 添加功能
            func(参数)
            # 添加功能

        return inner
"""

"""
from math import sqrt
# 开方函数
def func(x):
    return sqrt(x)
print(func(-4))
"""

"""
# 使用装饰器扩展 函数的功能
# 开方函数
from math import sqrt
def func(x):
    return sqrt(x)

# 定义装饰器函数 接收函数对象（被装饰的函数对象）作为参数
def decorator(f):
    # 定义内层函数 完成功能的扩展
    # 内函数的参数 和被装饰的函数的参数 保持一致
    def inner(x):
        x = abs(x)
        return f(x)

    return inner

inn = decorator(func)
print(inn(-4))
"""


# 装饰器语法糖
# 开方函数
from math import sqrt

# 定义装饰器函数 接收函数对象（被装饰的函数对象）作为参数
def decorator(f):
    # 定义内层函数 完成功能的扩展
    # 内函数的参数 和被装饰的函数的参数 保持一致
    count = 0
    def inner(x):
        nonlocal count
        count += 1
        print(f"当前函数被装饰了{count}次")
        x = abs(x)
        return f(x)

    return inner

@decorator # 装饰后，会把func函数对象作为参数传递给decorator，并且将decorator 返回的结果inner直接赋值给func
def func(x):
    return sqrt(x)

@decorator #  装饰后，会把power函数对象作为参数传递给decorator，并且将decorator 返回的结果inner直接赋值给func
def power(x):
    return pow(x, 2)

print(func(-4)) # 2.0
print(func(-4)) # 2.0
print(func(-4)) # 2.0
print(power(-4))
print(power(-4))
print(power(-4))