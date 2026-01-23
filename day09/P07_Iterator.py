"""
    迭代器
"""
"""
import os

for element in [1,2,3]:
    print(element)
for element in (1,2,3):
    print(element)
for key in {"one": 1, "two": 2}:
    print(key)
for char in "123":
    print(char)
    
with open("myfile.txt","w") as f:
    f.write("H\ne\nl\nl\no\n \nW\no\nr\nl\nd\n")
for line in open("myfile.txt"):
    print(line, end="")
os.remove("myfile.txt")
"""

"""
#2. 判断是否是可迭代对象（Iterable）
from collections.abc import Iterable

print(isinstance([], Iterable)) #True
print(isinstance((), Iterable)) #True
print(isinstance(set(), Iterable)) #True
print(isinstance({}, Iterable)) #True
print(isinstance("100", Iterable)) #True
print(isinstance(100, Iterable)) #False
"""

"""
#3. 判断是否是迭代器（Iterator）
from collections.abc import Iterator
print(isinstance([], Iterator)) # False
print(isinstance((), Iterator)) #False
print(isinstance(set(), Iterator)) #False
print(isinstance({}, Iterator)) #False
print(isinstance("100", Iterator)) #False
print(isinstance((x for x in range(10)), Iterator)) #True
"""

"""
list1 = [1, 2, 3]
# print(type(list1)) # <class 'list'>
# it = iter(list1)
# print(type(it)) # <class 'list_iterator'>
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it)) # StopIteration

for item in list1:
    print(item)
"""


# 对一个序列执行反向循环的迭代器
# 迭代器有两个基本的方法：iter() 和 next()，__iter__和__next__缺一不可
class ReverseIter:
    """对一个序列执行反向循环的迭代器"""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

rit = ReverseIter([1,2,3,4,5,6,7,8])
# it = iter(rit)
for item in rit:
    print(item)



