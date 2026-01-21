"""
    异常的传递
    try块嵌套：
        若内层出现了异常且在内层无法处理，会将异常一层一层向外传递，直到异常被处理或程序报错
"""

try:
    try:
        try:
            print(1 / 0)
        except NameError as e:
            print("第1层try")
    except TypeError as e:
        print("第2层try")
except ZeroDivisionError as e:
    print("第3层try")


def m3():
    print(1/0)


def m2():
    m3()


def m1():
    m2()

m1()