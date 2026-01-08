"""
    字符串类型
    不可变 有序
"""

str1 = "hello world"
print(type(str1))

print(str1[2:5]) # llo
print(str1[2:]) # llo world

print("hello" * 2) # hellohello

print("he" in str1) # True

# 原始字符串 r
print("hello\n world")
print(r"hello\n world") # hello\n world


