"""
    单分支
"""
from random import randint
price = 50
balance = randint(0, 100)
print(f"您当前余额为：{balance}")
if balance < price:
    print("余额不足，请充值")
print("欢迎下次光临")