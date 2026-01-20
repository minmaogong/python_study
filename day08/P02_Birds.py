"""
    愤怒的小鸟
"""
class Birds:
    """鸟类"""
    def __init__(self, name, color, skill_desc):
        self.name = name
        self.color = color
        self.skill_desc = skill_desc

    def fly(self):
        pass

    def call(self):
        pass

    def use_skill(self):
        print(f"{self.name}使用了技能：{self.skill_desc}")

class RedBirds(Birds):
    def __init__(self):
        super().__init__("红火", "红色", "正常攻击")

    def fly(self):
        print("正常飞行")

    def call(self):
        print("嘎嘎嘎")

class YellowBirds(Birds):
    def __init__(self):
        super().__init__("黄蜂", "黄色", "加速攻击")

    def fly(self):
        print("瞬间加速飞行")

    def call(self):
        print("吱吱吱")

class BlueBirds(Birds):
    def __init__(self):
        super().__init__("蓝冰", "蓝色", "分裂攻击")

    def fly(self):
        print("分裂多只鸟飞行")

    def call(self):
        print("叽叽叽")

class Obstacle:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def be_attacked(self, bird):
        print(f"{bird.name}向障碍物{self.strength}发起了攻击")
        bird.use_skill()
        if isinstance(bird, RedBirds):
            damage = 40 # 定义了一个函数属性（局部属性）
        elif isinstance(bird, YellowBirds):
            damage = 80
        else:
            damage = 30 * 3

        self.strength -= damage

        if self.strength <= 0:
            print("障碍物已被摧毁")
        else:
            print(f"障碍物{self.name}还剩{self.strength}生命值")

o1 = Obstacle("木头房子", 100)
b1 = RedBirds()
o1.be_attacked(b1)
b2 = YellowBirds()
o1.be_attacked(b2)

