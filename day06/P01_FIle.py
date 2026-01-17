"""
    文件的读写
"""

"""
# 文件的写入
# 打开文件
f = open("test.txt", "w")

# 写入操作
f.write("hello world \n")
f.write("你好 Python \n")

# 关闭文件
f.close()
"""

"""
# 文件读取
# 打开文件
f = open("test.txt", "r")

# 读取文件所有数据 read()
# print(f.read())

# 从文件中读取指定的字节数 read(size)
# print(f.read(5)) # hello
# print(f.read(4)) #  wor

# 从文件中读取一行数据 readline()
# print(f.readline()) # hello world
# 与read(size) 效果一样 readline(size)
# print(f.readline(5)) # hello

# 从文件中按行读取数据，存入列表中 readlines()
print(f.readlines()) # ['hello world \n', '你好 Python \n']


# 关闭文件
f.close()
"""

# 递归遍历目录的内容

import os
for root, dirs, files in os.walk(os.getcwd()):
    print("当前路径：", root)
    print("目录：", dirs)
    print("文件：", files)
    print()
