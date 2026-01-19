"""
    Self
"""

class Student:

    # 类属性
    school = "联合大学"

    def __init__(self, name, age):
        # 实例属性
        self.name = name
        self.age = age

    def study(self):
        self.eat() # Study.eat(self)
        print(f"{self.name}吃饱了，开始study ...")


    def eat(self):
        print("eat ...")


zhang_school = Student("zhang", 18)
zhang_school.study() # Student.study(zhang_school)