"""
    在子类中复用父类成员
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
        print("先吃点东西")
        # 1.通过super()方法访问父类成员
        # super().eat()
        # 2.通过父类名.成员名
        Person.eat(self)
        print("study...", super().home)


class ChineseStudent(Student, YellowRace):
    country = "China"

chinese_student = ChineseStudent("张三", "一年级")
chinese_student.study()