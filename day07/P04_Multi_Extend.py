"""
    继承：多继承
    调用方法时先在子类中查找，若不存在则从左到右依次查找父类中是否包含方法。
"""
"""
class Person:
    home = "earth"

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("eating...")

class YellowRace(Person):
    color = "yellow"

    def run(self):
        print("runing...")

class Student(Person):
 
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self):
        print("study...")


class ChineseStudent(Student, YellowRace):
    country = "China"

chinese_student = ChineseStudent("张三", "一年级")
print(chinese_student.home, chinese_student.color, chinese_student.country, chinese_student.name, chinese_student.grade)
chinese_student.eat()
chinese_student.run()
chinese_student.study()
"""

class Person:
    home = "earth"

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("eating...")


class YellowRace(Person):
    color = "yellow"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("runing...")

    def m1(self):
        print("yellowrace m1无参")


class Student(Person):

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self):
        print("study...")

    def m1(self):
        print("student m1无参")


class ChineseStudent(Student, YellowRace):
    country = "China"

    def __init__(self):
        print("init")

    def m1(self):
        print("m1无参")

    def m1(self, a):
        print("m1带参数")

    # def m1(self, *args):
    #     pass

chinese_student = ChineseStudent()
chinese_student.m1() # 报错 ChineseStudent.m1() missing 1 required positional argument: 'a' 因为在ChineseStudent类的命名空间中，m1引用会指向后创建的带参数的函数对象