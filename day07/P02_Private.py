"""
    封装： 属性和方法私有化
"""

# 私有化
# 1. 单下划线：非公开API。这种约定不具有强制力，依然可以访问
# 2. 双下划线：名称改写 例如__x，会被改写成 _类名__x。只有在类内部可以通过__x访问，其他地方无法访问或者通过_类名__x访问
"""
class Girl:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # 获取__age属性的值
    def get_age(self):
        if self.__age >= 18:
            return 18
        else:
            return self.__age

    # 设置__age属性的值
    def set_age(self, age):
        self.__age = age

zhang_san = Girl("张三", 30)
print(zhang_san.name)
# print(zhang_san._age)
print(zhang_san._Girl__age) # 通过 实例对象._类名__私有属性 是可以访问到__私有属性的
print(zhang_san.get_age())
"""

class Girl:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property # 将方法转换成属性的形式
    def eat(self):
        print("eating")

    @property
    def age(self):
        if self.__age >= 18:
            return 18
        else:
            return self.__age

    @age.setter # 设置属性
    def age(self, age):
        self.__age = age

zhang_san = Girl(name="zhang", age=20)
zhang_san.eat
zhang_san.age = 12
print(zhang_san.age)