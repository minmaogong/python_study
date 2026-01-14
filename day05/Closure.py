"""
    闭包
"""

def outer():
    num = 10

    def inner():
        print(num) # 因为闭包延长了外层函数局部变量的生命周期，和内函数绑定，当内函数执行完毕之后，对应的局部变量才会被释放

    return inner

a = outer()
print(type(a)) # <class 'function'>
outer()() # 10