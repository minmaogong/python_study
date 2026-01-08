"""
数据类型转换：
    自动类型转换（隐式转换）
    强制类型转换（显示转换）
"""

# 自动类型转换（隐式转换）
num1 = 10
num2 = 20
# 相同类型运算，不涉及类型转换
num3 = num1 + num2
print(type(num3)) # <class 'int'>

num4 = 10
f1 = 5.0
# 自动类型转换（隐式转换）：对于两种不同数据类型的数据进行运算，较小的数据类型（整型）就会转换为较大的数据类型（浮点型）以避免数据丢失，计算结果为浮点型
res = num4 + f1
print(res, type(res)) # 15.0 <class 'float'>

# 两个整型进行除法运算结果也是浮点型
num5 = 10
num6 = 2
num7 = num5 / num6
print(num7, type(num7)) # 5.0 <class 'float'>

"""
num8 = 10
str1 = "hello"
print(str1 + num8) # 会报错
"""

# 强制类型转换（显示转换）
# int(x [, base]) 将x转换为一个整数，x若为字符串可用base指定进制
print(int('101', 2)) # 1*2^2 + 0*2^1 + 1 = 5
print(int('102', 8)) # 1*8^2 + 0*8^1 + 2 = 66
print(int('10A', 16)) # 1*16^2 + 0*16^1 + 10 = 266

# float(x) 将x转换为一个浮点数
print(float('1.000')) # 1.0
print(float(5)) # 5.0

# complex(real [,imag]) 创建一个实部为real，虚部为imag的复数
print(complex(3, 2)) # (3+2j)

# str(x) 将对象x转换为一个字符串
print(str("hello\nworld")) # 会识别换行符，自动换行
# repr(x) 将对象x转化为一个字符串，可以转义字符串中的特殊字符
print(repr("hello \n world")) # 'hello \n world' 不会识别换行符，会将\n当作不同字符串输出

# eval(x) 执行x字符串表达式，并返回表达式的值
eval("print(123)") # 123

# bin(x) 将一个整数转换为一个二进制字符串
print(bin(10)) # 0b1010
# oct(x) 将一个整数转换为一个八进制字符串
print(oct(10)) # 0o12
# hex(x) 将一个整数转换为一个十六进制字符串
print(hex(10)) # 0xa

# ord(x) 将一个字符转换为它的ASCII整数值
print(ord('a')) # 97
print(ord(' ')) # 32

# chr(x) 将一个整数转换为一个Unicode字符
print(chr(65))  # A
print(chr(97 ))  # a

# tuple(s) 将序列s转换为一个元组
# list(s) 将序列s转换为一个列表
# set(s) 转换s为可变集合