from collections.abc import Iterator

# 迭代器有两个基本的方法：iter() 和 next()
class MyTest:
    def __iter__(self):
        return self

    def __next__(self):
        pass

mt = MyTest()
print(isinstance(mt, Iterator)) # True