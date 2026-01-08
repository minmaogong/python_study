"""
 字符编解码
"""

# 编码：将字符转换为字节的过程
str1 = "你好"
byte1 = str1.encode(encoding='utf-8')
print(byte1) # b'\xe4\xbd\xa0\xe5\xa5\xbd'
# 解码：将字节转换为字符的过程
print(type(byte1)) # <class 'bytes'>
print(byte1.decode(encoding='utf-8')) # 你好