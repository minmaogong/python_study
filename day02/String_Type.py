"""
字符串类型
"""

str1 = 'This is a "string"'
str2 = "This is a 'string' too"
print(type(str1)) # <class 'str'>
print(str1, str2) # This is a "string" This is a 'string' too

# 三引号，原样输出字符串内容，所见即所得
str3 = '''
    hello world!
        hello python!
    !!!!!!
'''
print(str3)

# \  在行尾作为续行符
str4 = ("hello \
        world")
print(str4)

str5 = "hello\nworld"
print(str5)
str6 = "hello\rworld"
print(str6) # world

# 字符串的intern机制：每个字符串，不夹杂空格或者特殊字符号，默认开启intern机制，共享内存，靠引用计数决定是否销毁
str7 = "hello world"
str8 = "hello world"
print(id(str7), id(str8)) # 4346656496 4346656496

str9 = "zs\tls\tww"
print(str9) # zs	ls	ww