"""
    return
"""

def print_star():
    """打印*"""
    print("*"*20)
    # return



print(print_star()) # None


def sum1(num1, num2):
    """计算两个整数的和"""
    return num1 + num2

print(sum1(2, 3)) # 5


# return 返回多个值
def func(a, b, c):
    return  a, b, c, [a, b, c] # 以元组的方式返回多个值

print(func(1, 2, 3)) # (1, 2, 3, [1, 2, 3])