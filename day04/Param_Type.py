# 不定长参数
# 形式一：*参数名    可以接收多个参数，底层是将多个参数放到元组中进行处理
def print_info(num, *var):
    print(num)
    print(var, type(var))  # (20, 30, 40) <class 'tuple'>


print_info(10, 20, 30, 40)


# 不定长参数
# 方式二：  **参数名   底层是通过字典对传递的参数进行封装处理
# 注意：如果是两个*的不定长参数，后面不能再出现普通参数了
def print_info2(num, **var):
    print(num)
    print(var, type(var))  # {'a': 20, 'b': 30} <class 'dict'>


print_info2(10, a=20, b=30)


# 解包传参
def print_info3(a, b, c):
    print(a, b, c)  # 1 2 3                10 20 30              100 200 300


tup1 = (1, 2, 3)
print_info3(*tup1)  # 通过*解包

dict1 = {'a': 10, 'b': 20, 'c': 30}
print_info3(**dict1)  # 通过**解包

list1 = [100, 200, 300]
print_info3(*list1)  # 通过*解包


# / 前的参数必须使用位置传参，* 后的参数必须使用关键字传参
def print_info4(a, b, /, c, d, e, *, f, g):
    print(a, b, c, d, e, f, g)

print_info4(1, 2, 3, 4, 5, f=6, g=7)