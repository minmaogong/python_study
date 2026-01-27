"""
    装饰器参数
"""
from math import sqrt

def xx(n):
    def get_absolute(f):
        def inner(x):
            x = abs(x)
            for i in range(n):
                x = f(x)
            return x
        return inner
    return get_absolute

@xx(n=2)
def func(x):
    return sqrt(x)


print(func(81))
# inn = xx(2)(func)
# print(inn(81))
# print(xx(2)(func)(81))

