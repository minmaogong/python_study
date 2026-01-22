"""
    模块的导入
"""

# 全局导入：导入模块的所有成员
# import P02_my_add
# print(P02_my_add.num)
# print(P02_my_add.add(3, 5))

"""
import P02_my_add as my_add
print(my_add.num)
print(my_add.add(3, 5))
"""


# 局部导入
# 方式1 from import : 从模块中指定导入模块的部分成员
"""
from P04_my_multi import multi
print(multi(3, 4)) # 12
"""

# 重名变量，后一次的导入会覆盖前一次导入
"""
from P02_my_add import num as n1
from P04_my_multi import num as n2
# print(num) #200
print(n1) # 100
print(n2) # 100

# 方式2 from import *   : 导入模块中所有不以单下划线开头的成员，直接通过成员名的方式访问
from P04_my_multi import *
print(num)
print(multi(3, 4))
# print(_str1) # 访问不到
"""


# 模块搜索顺序
"""
import sys

print(sys.path)
sys.path.append("./..") # 临时添加路径
print(sys.path)
"""


# __all__ 限制被导入的成员
"""
from P02_my_add import *

print(num)
# print(num1) # 因为P02_my_add模块中定义了__all__，__all__列表中没有num1，所以访问不了
# print(_str1)
print(add(10, 20))
"""

"""
# dir()
# 当将第一个模块作为dir()的参数时，它会返回该模块中定义的名称列表，包括函数、类、变量等 dir(模块名)
import random
print(dir(random))
"""
"""
# 当将一个对象作为dir()的参数时，它会返回该对象的属性和方法列表
class MyClass:
    def __init__(self):
        self.x = 1
        self.y = 2

    def method(self):
        pass

obj = MyClass()
print(dir(obj))
"""

# 当不传递任何参数调用dir()时，它会列出当前作用域中定义的名称，包括变量、函数、类等
def m1(aa, bb):
    print(dir()) # ['aa', 'bb']

m1(1, 2)
