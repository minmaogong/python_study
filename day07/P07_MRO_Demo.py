"""
    MRO的Demo
"""
"""
class Parent1:
    def __init__(self, value1):
        print("Initializing Parent1")
        self.value1 = value1

class Parent2:
    def __init__(self, value2):
        print("Initializing Parent2")
        self.value2 = value2


class Child(Parent1, Parent2):
    def __init__(self, value1, value2):
        print("Initializing Child")
        Parent1.__init__(self, value1)
        Parent2.__init__(self, value2)


child = Child("v1", "v2")
print(child.value1)
print(child.value2)
"""

"""
class Parent1:
    def __init__(self, value1):
        print("Initializing Parent1")
        self.value1 = value1

class Parent2:
    def __init__(self, value2):
        print("Initializing Parent2")
        self.value2 = value2


class Child(Parent1, Parent2):
    def __init__(self, value1, value2):
        print("Initializing Child")
        super().__init__(value1)
        # super().__init__(value2) # 其实调用的都是Parent1的__init__，所以print(child.value2)会报错，value2没有被赋值
        # 调用 Parent2 的 __init__方法， 从Parent1 之后开始查找 MRO 链，调用一下父类（即Parent2）的__init__方法，把value2 传给Parent2
        super(Parent1, self).__init__(value2)


child = Child("v1", "v2")
print(child.value1)
print(child.value2)
"""

class GrandParent:
    def __init__(self):
        print("Initializing GrandParent")

class Parent1(GrandParent):
    def __init__(self):
        super().__init__()
        print("Initializing Parent1")

class Parent2(GrandParent):
    def __init__(self):
        super().__init__()
        print("Initializing Parent2")

# class Child(Parent1, Parent2):
#     def __init__(self):
#         Parent1.__init__(self) # 使用父类名.__init__会存在重复初始化问题
#         Parent2.__init__(self)

class Child(Parent1, Parent2):
    def __int__(self):
        # 仅需调用一次super(). MRO 自动处理所有父类/祖父类
        super().__init__() # 使用super()， 会自动使用 MRO 链 查找父类，即 Parent1 -> Parent2 -> GrandParent，不会重复初始化

child = Child()