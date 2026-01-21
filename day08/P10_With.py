"""
    with: 底层对try...finally 进行封装，一般用于资源的释放
    语法：
        with expression as variable:
            # 代码块
    说明：
        expression：通常是一个对象或函数调用，该对象需要是一个上下文管理器，即实现了__enter__和__exit__方法
        variable：是可选的，用于存储expression的__enter__方法的返回值
"""

"""
try:
    f = open("test.txt", "w")
    f.write(a)
    f.close()
finally:
    print(f.closed)
"""
"""
try:
    f = open("test.txt", "w")
    try:
        f.write(a)
    except:
        print("error")
    finally:
        f.close()
finally:
    print(f.closed)
"""

try:
    with open("test.txt", "w") as f:
        f.write(a)
# except:
#     print("error")
finally:
    print(f.closed)