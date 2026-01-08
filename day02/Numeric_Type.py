from decimal import Decimal

"""
数值类型: int整型、float浮点型、bool布尔型
"""

# 整数类型
num1 = 1_000_000_000_000_000
print(num1, type(num1)) #1000000000000000  <class 'int'>
print(isinstance(num1, float)) # False
print(isinstance(num1, bool)) # False
print(isinstance(num1, int)) # True
print(isinstance(num1, str)) # False

num2 = True
print(isinstance(num2, int)) # True Python3中，bool是int的子类
print(isinstance(num2, bool)) # True
print(type(num1) == type(num2)) # False type()只比较类型，不关心继承关系

# 小整数池 [-5, 256] 注意： CPython的默认实现，不同环境不同解释器优化机制不同
num3 = 10 # 直接指向小整数池中的 10，不需要在内存中分配空间，避免频繁创建和销毁
num4 = 10 # 直接指向小整数池中的 10，不需要在内存中分配空间，避免频繁创建和销毁
num5 = 10 # 直接指向小整数池中的 10，不需要在内存中分配空间，避免频繁创建和销毁

# id() 查看变量的内存地址
print(id(num3), id(num4), id(num5)) # 4356695320 4356695320 4356695320 指向相同的地址

# 大整数池，一开始为空，没创建一个大整数，就会向池中存储一个 注意：不同环境不同解释器优化机制不同
num6 = 300
num7 = 300
print(id(num6), id(num7)) # 4372830672 4372830672 指向大整数池同一个地址



# 浮点类型
f1 = 0.1
f2 = 0.2
print(type(f1), type(f2)) # <class 'float'> <class 'float'>
f3 = f1 + f2
print(f3) # 0.30000000000000004

# 通过Decimal解决精度问题
f4 = Decimal('0.1')
f5 = Decimal('0.2')
print(type(f4), type(f5)) # <class 'decimal.Decimal'> <class 'decimal.Decimal'>
f6 = f4 + f5
print(f6) # 0.3



# bool类型
b1 = True
b2 = False
print(type(b1), type(b2)) # <class 'bool'> <class 'bool'>
print(b1 == 1) # True
print(b2 == 0) # True
print(b1 + 10) # 11
# is: 判断b1 和 1 是不是同一个对象（是不是执行内存中的同一个地址）
print(b1 is 1) # False
print(b2 is 0) # False