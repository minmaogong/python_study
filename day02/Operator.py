"""
    运算符
"""

# 算数运算符
# + 加
print(1 + 2)
# - 减、或取负
print(1 - 2)
# * 乘
print(2 * 3)
# / 除
print(3 / 2) # 1.5
# // 整除，除后向下取整
print(3 // 2) # 1
# % 模，返回除法的余数
print(8 % 3) # 2
# ** 幂
print(2 ** 3) # 8

print("#################################")

# 赋值运算符
# = 赋值
a = 1
print(a)
# += 加法赋值
a += 1
print(a)
# -= 减法赋值
a -= 1
print(a)
# *= 乘法赋值
a *= 5
print(a)
# /= 除法赋值
a /= 2
print(a) # 2.5
# //= 整除赋值
a = 5
a //= 2
print(a) # 2
# %= 模赋值
a = 14
a %= 5
print(a) # 4
# **= 幂赋值
a = 3
a **= 3
print(a) # 27
# := 海象运算符
num1 = 10
num2 = 20
print(num3 := num1 + num2) # 30


print("#############################")
# 比较运算符 == != > < >= <=


print("#############################")
# 逻辑运算符
# and 与， x and y，若x为false返回x的值，否则返回y的值
x = 0
y = 8
print(x and y) # 0
# or 或，x or y，若x为true返回x的值，否则返回y的值
print(x or y) # 8
# not 非，not x，若x为true返回false，若x为false返回true
print(not x, not y) # True False



print("#############################")
# 位运算符
# & 按位与
# ｜ 按位或
# ^ 按位异或
# ~ 按位取反
# << 按位左移
# >> 按位右移



print("#############################")
# 成员运算符
list1 = [10, 20, 30]
print(10 in list1) # True
print(10 not in list1) # False


print("#############################")
# 身份运算符
num1 = 10
num2 = 10
print(num1 is num2) # True
print(num1 is not num2) # False


print("#############################")

