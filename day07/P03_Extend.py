"""
    继承： 单继承
"""
# 单继承
class Person:
    """人的类"""
    # Person类的类属性
    home = "earth"
    def __init__(self, name):
        # 实例属性
        self.name = name

    # 实例方法
    def eat(self):
        print("eating")

class YellowRace(Person):
    # YellowRace类的类属性
    color = "yellow"

class WhiteRace(Person):
    # WhiteRace类的类属性
    color = "white"

class BlackRace(Person):
    # BlackRace类的类属性
    color = "black"

yellowRace = YellowRace(name="张三")
print(yellowRace.color, yellowRace.name, yellowRace.home)
yellowRace.eat()

whiteRace = WhiteRace(name="Mike")
print(whiteRace.color, whiteRace.name, whiteRace.home)
whiteRace.eat()

blackRace = BlackRace(name="James")
print(blackRace.color, blackRace.name, blackRace.home)
blackRace.eat()