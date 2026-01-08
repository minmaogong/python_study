"""
    字符串常用好书
"""

str1 = "hello world"
print(str1)

# replace
str2 = str1.replace("world", "python")
print(str1, str2) # hello world hello python

# split
str3 = "id,name,age,gender"
print(str3.split(",")) # ['id', 'name', 'age', 'gender']
print(str3.split(",", 2)) # ['id', 'name', 'age,gender']

# rsplit
print(str3.rsplit(",")) # ['id', 'name', 'age', 'gender']
print(str3.rsplit(",", 2)) # ['id,name', 'age', 'gender']

# join
print("_".join(["1", "2", "3", "4"])) # 1_2_3_4

# strip 截掉字符串两边的空格或指定字符串
str4 = "           hello        "
print(str4.strip()) # hello
str4 = "xxxxxxxxxhelloxxxxxx"
print(str4.strip("x")) # hello
print(str4.rstrip("x")) # xxxxxxxxxhello
print(str4.lstrip("x")) # helloxxxxxx

# removeprefix() 截掉字符串前缀
print(str4.removeprefix("xxxxxxxx")) # xhelloxxxxxx
# removesuffix() 截掉字符串后嘴
print(str4.removesuffix("oxxxxxx")) # xxxxxxxxxhell

# upper
print("hello".upper()) # HELLO

# lower
print("HELLO".lower()) # hello

# swapcase() 反转字符串字母大小写
print("Hello".swapcase()) # hELLO 反转字符串字母大小写

# capitalize 将字符串第一个字母变为大写，其他变为小写
print("heLlo".capitalize()) # Hello

# title 将每个单词首字母大写
print("hello world".title()) # Hello World

print(len("hello")) # 5

print(max("hello")) # o
print(min("hello")) # e

# find()
print("hello".find("h")) # 0
print("hello".find("h" , 2)) # -1

# rfind()
print("hello".rfind("h"))

print("hello".count("l")) # 2

# isspace 检查字符串是否非空且只包含空白
print("".isspace()) # False
print("  ".isspace()) # True
print(" abc ".isspace()) # False

# isalnum 检查字符串是否非空且只包含字母中（英文字母和汉字）和数字
print("hello123".isalnum()) # True
print("hello123@#!".isalnum()) # False

# isalpha 检查字符串是否非空且只包含字母（英文字母和汉字）
print("hello你好".isalpha()) # True
print("hello123".isalpha()) # False

# isascii 检查字符串是否只包含ASCII字符，空字符串也是ASCII
print("hello".isascii()) # True
print("你好".isascii()) # False
print("".isascii()) # True

# isdecimal 检查字符串是否非空且只包含十进制字符
print("123".isdecimal()) # True
print("123abc".isdecimal()) # False
print("一二三".isdecimal()) # False

# *isdigit 检查字符串是否非空且只包含数字 一般用这个
print("123".isdigit()) # True
print("一二三".isdigit()) # False

# isnumeric 检查字符串是否非空且只包含数值字符
print("123".isnumeric()) # True
print("一二三".isnumeric()) # True