class Person:
    """人的类"""

    # 类属性 --- 直接定义在类下的变量，当前这个类创建出来的所有实例共享
    home = "earth"

    # 魔法方法 创建对象的时候执行的方法
    def __init__(self, name, age):
        # self 表示当前创建出来的对象      在__init__方法中，一般定义实例属性，并进行初始化

        #实例属性       每一个实例独有，互相隔离
        self.name = name
        self.age = age


    #实例方法
    def eat(self):
        print("eating")




# 类的操作
# 成员引用      类名.成员名
home = Person.home
eat = Person.eat
print(home) # earth
print(eat) # <function Person.eat at 0x00000220ABC42660>
print(Person.__doc__) # 人的类

# 实例化
# 当我们创建对象的时候，底层会自动调用__init__方法
person = Person("ZhangSan", 30)
print(person.home) # 类属性 earth
# 实例属性
print(person.name, person.age)
# 实例方法调用
person.eat() # eating