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



# 提供函数 生成斐波那契数列
"""
def feibo(n):
    a, b, i = 0, 1, 1
    while i <= n:
        print(b)
        a, b, i = b, a + b, i + 1

f= feibo(10)
print(type(f)) # <class 'NoneType'>
"""




# 方式2：使用生成器函数 创建生成器对象
def feibo():
    a, b = 0, 1
    while(True):
        yield b
        a, b = b, a + b

f = feibo()
print(type(f)) # <class 'generator'>
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
