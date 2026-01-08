"""
    match case 语句
"""
from random import randint

month = randint(1,12)
print(f"当前月份是：{month}")

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(f"{month}月有31天")
    case 4 | 6 | 9 | 11:
        print(f"{month}月有30天")
    case _:
        print(f"{month}月有28天")
