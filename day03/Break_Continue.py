"""
    break continue pass
    break: 跳出整个循环
    continue: 跳出当前执行的循环，继续下一次循环
    pass: 空语句，是为了保持程序的完整性，不做任何事情，一般用作占位语句
"""

for i in range(10):
    if i == 3:
        continue
    if i == 5:
        break
    print(i, end=" ") # 0 1 2 4

for i in range(10):
    pass # 占位语句
