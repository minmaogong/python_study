"""
    生成器的创建
"""
from collections.abc import Iterator

# 方式1: 推导式

gen = (i for i in range(5))
print(type(gen)) # <class 'generator'>
print(isinstance(gen, Iterator)) # True
print(next(gen)) # 0
print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3
print(next(gen)) # 4
# print(next(gen)) # 抛异常 StopIteration