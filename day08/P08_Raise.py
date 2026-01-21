"""
    raise 抛出异常
"""

def add(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        # 抛出异常
        raise TypeError("参数必须传递整数")


try:
    print(add(1, "2"))
except TypeError as e:
    print(e)

class MyException(Exception):
    pass

def welcome(name, age):
    if 0 <= age <= 200:
        print("Hello", name, "!", age)
    else:
        raise MyException("年龄必须在0-200之间")

welcome("张三", 300)

# 断言
def add1(a, b):
    assert isinstance(a, int) and isinstance(b, int), "参数必须传递整数"
    return a + b

add1(1, "20")