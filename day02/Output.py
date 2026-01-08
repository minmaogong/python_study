"""
    输出
"""

# end控制输出结尾
print("hello", end=' ')
print("world") # hello world

str1 = "hello"
byte1 = str1.encode(encoding='utf-8')
print(byte1) # b'hello'
print(list(byte1)) # [104, 101, 108, 108, 111]

# 格式化输出
# 1.字符串中使用 % 占位
int1 = 10
float1 = 3.14
str1 = "int1 = %d float1 = %.2f" %(int1, float1)
print(str1) # int1 = 10 float1 = 3.14

# 2.字符串.fromat()
int2 = 30
float2 = 3.14
# 方式1: 不设置指定位置， 按默认顺序
str2 = "int2={}, float2={}".format(int2, float2)
print(str2) # int2=30, float2=3.14
# 方式2: 设置指定位置，不能和方式1混合使用
str3 = "int2={1}, float2={0}".format(float2, int2)
print(str3) # int2=10, float2=3.14
# 方式3: 设置参数
str4 = "int2={a}, float2={b}".format(a = int2, b = float2)
print(str4) # int2=30, float2=3.14


# 数字的格式化
float2 = 31415.0
str5 = "{:*^20,.2f}".format(float2)
print(str5) # *****31,415.00******
str6 = "{:*<20.2f}".format(float2)
print(str6) # 31415.00************
str7 = "{:#>20,.2f}".format(float2)
print(str7) # ###########31,415.00

# f-字符串
int3 = 30
float3 = 3.14
str8 = f"int3={int3}, float3={float3}"
str9 = f"{int3 = }, {float3 = }"
print(str8) # int3=30, float3=3.14
print(str9) # int3 = 30, float3 = 3.14