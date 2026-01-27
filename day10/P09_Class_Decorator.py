"""
    类装饰器
    类装饰器是包含 __call__() 方法的类，它接受函数作为参数，并返回新的函数
"""


"""
from math import sqrt

def func(x):
    return sqrt(x)

class MyClass:
    def __call__(self):
        print("call")

mc = MyClass()
mc()
"""

from math import sqrt

class DecoratorClass:
    def __init__(self, f):
        self.f = f

    def __call__(self, x):
        x = abs(x)
        return self.f(x)

@DecoratorClass #func 函数对象作为参数传给DecoratorClass的init方法，DecoratorClass会将实例对象赋值给func，func(-4) 实际是调用了DecoratorClass的__call__() 魔法方法
def func(x):
    return sqrt(x)

# dc = DecoratorClass(func)
# print(dc(-4))

print(type(func), func(-4)) # <class '__main__.DecoratorClass'> 2.0