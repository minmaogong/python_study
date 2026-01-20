
"""
# 编写一个函数，接受一个整数作为参数，返回该整数的反转形式，例如，输入123，返回321；输入-456，返回-654

def reverse_number(num):
    if num < 0:
        # 负数
        str_num = str(-num)
        str_num = str_num[::-1] # 切片 [::-1] 从后往前切 [::1] 从前往后切
        return - int(str_num)
    else:
        # 正数
        str_num = str(num)
        str_num = str_num[::-1]
        return int(str_num)


print(reverse_number(123))

"""
import math
import types

"""
# 有一个嵌套字典，存储了学生的课程成绩信息。编写一个函数，计算每个学生的平均成绩，并返回一个新的字典，键为学生的名字，值为平均成绩
students = {
    "Alice": {
        "Math": 85,
        "English": 90,
        "Science": 78
    },
    "Bob": {
        "Math": 92,
        "English": 88,
        "Science": 95
    },
    "Charlie": {
        "Math": 70,
        "English": 75,
        "Science": 80
    }
}

def avg_score(students):
    result = {}
    for name, stu in students.items():
        # result[name] = round(sum(stu.values()) / len(stu), 2)
        result[name] = "{:.2f}".format(sum(stu.values()) / len(stu))
    return result

print(avg_score(students))
"""


# 题目 1：动态添加属性
# 定义一个 Person 类，在类外动态地给 Person 类的一个对象添加一个 hobby 属性，值为 “reading”，并打印该属性。
class Person:
    pass

p = Person()
p.hobby = "reading"
print(p.hobby)

# 题目 2：动态添加方法
# 定义一个 Circle 类，该类有一个 radius 属性。在类外定义一个函数 calculate_area，功能是计算圆的面积（面积公式：(S = π r^2），然后将这个函数动态地添加为 Circle 类的一个对象的方法，并调用该方法计算半径为 5 的圆的面积。（提示：可使用 types.MethodType）
"""
class Circle:
    def __init__(self, radius):
        self.radius = radius

def calculate_area(self):
    return math.pi * (self.radius ** 2)

circle = Circle(5)
circle.func = types.MethodType(calculate_area, circle)
print(circle.func())
"""



# 题目 3：封装特性
# 定义一个 BankAccount 类，有一个私有属性 __balance（初始余额为 0），提供一个 deposit 方法用于存钱，一个 withdraw 方法用于取钱，取钱时如果余额不足则打印提示信息。
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, money):
        self.__balance += money
        print(f"存款{money}，当前余额{self.__balance}")

    def withdraw(self, money):
        if money > self.__balance:
            print("余额不足")
        else:
            self.__balance -= money
            print(f"取款{money}，当前余额{self.__balance}")

ba = BankAccount()
ba.deposit(100)
ba.withdraw(1000)

# 题目 4：多态特性
# 定义一个 Shape 类，有一个抽象方法 area（方法体为空）。
# 再定义 Rectangle 类和 Circle 类继承自 Shape 类，分别实现 area 方法计算矩形面积（长 × 宽）和圆的面积（(\pi r^2)）。
# 创建 Rectangle 和 Circle 类的对象，将它们放入一个列表中，遍历列表并调用每个对象的 area 方法。
from abc import abstractmethod, ABC
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

rectangle = Rectangle(5, 10)
circle = Circle(5)
list1 = [rectangle, circle]
for item in list1:
    print(item.area())
