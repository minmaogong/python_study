"""

"""
# 编写一段 Python 代码，尝试将字符串“123abc”转换为整数，如果转换失败，捕获ValueError异常，将异常信息记录到一个文本文件error.log中
"""
str1 = "123abc"
try:
    int1 = int(str1)
except ValueError as e:
    with open("error.log", "w") as f:
        f.write(str(e))
"""


# 定义一个函数check_age,该函数接受一个年龄参数。如果年龄小于0，抛出一个自定义异常InvalidAgeError;
# 如果年龄大于120，抛出UnrealisticAgeError。这两个自定义异常类都继承自Exception类。调用该函数并传入一个不合法的年龄值，捕获并处理异常。
class InvalidAgeError(Exception):
    pass

class UnrealisticAgeError(Exception):
    pass

def check_age(age):
    if age <= 0:
        raise InvalidAgeError("InvalidAgeError")
    elif age >= 120:
        raise UnrealisticAgeError("UnrealisticAgeError")

try:
    check_age(120)
except InvalidAgeError as e:
    print(e)
except UnrealisticAgeError as e:
    print(e)
