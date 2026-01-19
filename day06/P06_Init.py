"""
    对象的创建过程
"""

class Student:
    #类属性
    school = "联合大学"

    def __init__(self, name, age):
        # 定义实例属性
        self.name = name
        self.age = age

    def study(self):
        print(f"{self.name} is studying")


zhang_san = Student("zhangsan", 18)
print(zhang_san.school)
print(zhang_san.name)
print(zhang_san.age)
zhang_san.study() # Student.study(zhang_san)