"""
    局部作用域：函数内
    嵌套作用域：闭包内
    全局作用域：模块内
    内建作用域：BuildIn
"""

var1 = 100
def func():
    """在局部作用域中使用global关键字可以为全局变量赋值"""
    # var1 = 200 # 在局部作用域中重新创建了一个var1变量，赋值不会影响全局变量var1
    global var1 # global关键字表示var1是全局变量
    var1 += 10 # 直接对全局变量赋值操作
    print(var1) # 110

func()
print(var1) # 110



def outer():
    num1 = 10
    def inner():
        # num1 = 100 // 在局部作用域中重新创建了一个num1变量，赋值不会影响嵌套作用域变量num1
        nonlocal num1 # nonlocal关键字表示num1是嵌套作用域中的变量
        num1 = 100 # 直接对嵌套作用域变量进行赋值操作
        print(f"局部{num1}")

    inner()
    print(f"嵌套{num1}")


outer()