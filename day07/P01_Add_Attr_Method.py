"""
    动态添加属性和方法
"""
import types


class Person:
    def __init__(self, name):
        self.name = name

# 动态给对象添加属性
p1 = Person("zhang_san")
print(p1.name) # zhang_san
p1.age = 18 # 动态给对象添加属性
print(p1.age) # 18

# p2 = Person("li_si")
# print(p2.age)

# 动态给类添加属性
Person.school = "联合大学"
print(p1.school) # 联合大学

# 动态给实例添加方法
def eat():
    print("eat ...")

p1.eatSomething = eat
p1.eatSomething() # eat ...

# 添加实例方法
def drink(self):
    print(f"{self.name} drinking...")

# p1.dk = drink
# p1.dk(p1)
p1.dk = types.MethodType(drink, p1) # 给指定实例绑定方法
p1.dk() # zhang_san drinking...


# 动态给类添加类方法
@classmethod
def come_from(cls):
    print(f"come from {cls.home} ")

@staticmethod
def static_function():
    print("static_function...")

Person.home = "earth"
Person.come_from = come_from
Person.come_from() # come from earth

# 动态给类添加静态方法
Person.static_func = static_function
Person.static_func() # static_function...


# 动态删除属性和方法
# del p1.name
# print(p1.name)
# delattr(p1, "name")
# print(p1.name)


class Person1:
    # 定义 动态添加属性和方法 的限制
    __slots__ = ("name", "age", "eat")

    def __init__(self, name=None):
        self.name = name

def eat(self):
    print(f"{self.name} eat ...")

def drink(self):
    print(f"{self.name} drinking...")

p3 = Person1("张三")
p3.age = 10
print(p3.age) # 10

# p3.gender = "male" # 超出限制，不能添加
# print(p3.gender)

p3.eat = types.MethodType(eat, p3)
p3.eat() # 张三 eat ...

# p3.drink = types.MethodType(drink, p3)
# p3.drink() # 超出限制，不能添加