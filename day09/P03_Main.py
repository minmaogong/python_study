"""
    模块的导入
"""

# 全局导入：导入模块的所有成员
# import P02_my_add
# print(P02_my_add.num)
# print(P02_my_add.add(3, 5))

import P02_my_add as my_add
print(my_add.num)
print(my_add.add(3, 5))


# 局部导入
# 方式1 from import : 从模块中指定导入模块的部分成员
from P04_my_multi import multi
print(multi(3, 4)) # 12

# 重名变量，后一次的导入会覆盖前一次导入
from P02_my_add import num as n1
from P04_my_multi import num as n2
# print(num) #200
print(n1) # 100
print(n2) # 100

# 方式2 from import *   :
