"""
    方法
"""

# 实例方法
# 实例方法中定义，第一个参数位self，代表实例本身
# 实例方法只能被实例对象调用
# 可以访问实例属性、类属性、类方法

"""
class Student:
    school = "联合大学"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def play_game(self):
        print(f"{self.age}岁的{self.name}正在{self.school}聚精会神的玩着游戏")

zhang_san = Student("zhang_san", 20)
zhang_san.play_game()
"""

# 类方法
# 类方法在类中通过 @classmethod 定义，第一个参数为cls，代表类本身
# 类方法可以被类和实例对象调用
# 可以访问类属性
# 在不创建实例的情况下调用，通过类名直接调用，非常方便，适合一些和类整体相关的操作
"""
class Student:
    school = "联合大学"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def study(cls):
        print("study ...") # study ...
        print(cls.school) # 联合大学
        print(cls.__doc__) # 学生类

li_si = Student("li_si", 20)
# li_si.study()
Student.study()
"""


# 静态方法
# 静态方法在类中通过 @staticmethod 定义
# 不访问实例属性或类属性，只能依赖于传入的参数
# 可以通过类名或实例调用，但它不会访问类或实例的内部信息，更像是一个工具函数，只是为了方便组织代码，把它放在了类里面
"""
class Student:
    school = "联合大学"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def static_method():
        print("static_method ...")

Student.static_method()
Student("zhang_san", 20).static_method()
"""

"""
# 在类外定义的函数
def f1(self, x, y):
    print(x + y)


class C:
    # f = f1
    f = lambda self, x, y: x + y


print(C().f(6, 13))
"""

class Student:
    def __new__(cls, *args, **kwargs):
        print("__new__")
        return super(Student, cls).__new__(cls)

    def __init__(self, name, age):
        print("__init__")
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age})"

    def __del__(self):
        print("__del__")

s1 = Student("shang_san", 20)
# del s1
print(str(s1)) # Name: shang_san, Age: 20
print(repr(s1)) # Student(name=shang_san, age=20)
ss = repr(s1) # Student(name=shang_san, age=20)
s2 = eval(ss) # 执行字符串表达式，并返回表达式的值
print(type(s2), s2) # <class '__main__.Student'> Name: shang_san, Age: 20

# 魔法方法（特殊方法）
# 1. __new__()
# 对象实例化时第一个调用的方法
# 2. __init__()
# 类的初始化方法
# 3. __del__()
# 对象的销毁，定义了当对象被垃圾回收时的行为。使用 del xxx 时不会主动调用__del__()，除非此时引用计数==0
# 4. __str__()
# 定义了对类的实例调用str()时的行为
# 5. __repr__()
# 定义对类的实例调用 repr() 时的行为。str() 和 repr() 最主要的差别在于目标用户。repr() 的作用时产生机器可读的输出（大部分情况下，其输出可以作为有效的Python代码），而str()则生产人类可读的输出
# 6. __getattribute__()
# 属性访问拦截器，定义了属性被访问前的操作