"""
    While循环
"""
import time

week = 1
rabbit = 2
while week <  10:
    week += 1
    rabbit = rabbit + rabbit * 2
print(f"第{week}周有{rabbit}只兔子")  # 第10周有39366只兔子



# 模拟进度条
num = 1
while num <= 50:
    print("\r" + "=" * num, end='') # \r 回到行首 end='' 输出不换行
    num += 1
    time.sleep(0.1)


# while ... else
while week <  10:
    week += 1
    rabbit = rabbit + rabbit * 2
else:
    print(f"第{week}周有{rabbit}只兔子")  # 第10周有39366只兔子
