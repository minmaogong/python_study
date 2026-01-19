"""
    属性
"""

# 类属性
"""
class Person:
    # 类属性 定义在类中，方法外
    home = "earth"


# 1.通过 类名.属性名 或 实例名.属性名 访问
print(Person.home)
print(Person().home)

# 2. 通过 类名.属性名 添加与修改类属性
Person.home = "地球"
Person.home123 = "地球123"
print(Person.home, Person.home123) # 地球 地球123

# 3. 使用 实例名.属性名 则会创建或修改实例属性         所以：类属性和实例属性不要同名
p1 = Person()
p2 = Person()
print(p1.home) # 地球
print(p2.home) # 地球
print("~" * 20)
p1.home = "火星"
print(p1.home) # 火星
print(p2.home) # 地球
print(Person.home) # 地球
"""


# 实例属性
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 1.通过 实例名.属性名 访问
p1 = Person("zhang_san", 18)
print(p1.name, p1.age) # zhang_san 18
# 2.通过 实例名.属性名 添加与修改实例属性
p1.gender = "male"
p1.age = 20
print(p1.name, p1.age, p1.gender) # zhang_san 20 male
