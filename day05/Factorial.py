"""
    递归
    求一个整数n的阶乘    5*4*3*2*1
"""

# 方式1: 循环实现
def get_factorial1(n):
    res = 1
    for i in range(n, 0, -1):
        res *= i
    return res

print(get_factorial1(5))


# 方式2：递归实现
def get_factorial2(n):
    if n == 1:
        return 1
    return n * get_factorial2(n - 1)

print(get_factorial2(5))