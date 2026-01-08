"""
    set 集合
    可变 无序 数据不重复
"""

# 创建集合对象
set1 = {1, 2, 3}
print(set1, type(set1)) # {1, 2, 3} <class 'set'>

list1 = [1, 2, 2, 3, 3, 3]
set2 = set(list1)
print(set2) # {1, 2, 3}

set3 = {} # 注意：{} 代表字典，不能表示空集合
print(type(set3)) # <class 'dict'>

set4 = set() # 创建空集合只能使用set()
print(type(set4)) # <class 'set'>

list2 = [1, 2, 3, 4, 5]
set5 = {i * 2 for i in list2} # 集合推导式
print(set5) # {2, 4, 6, 8, 10}

# 添加元素
set6 = {1, 2, 3}
print(hex(id(set6)), set6) # 0x102e45460 {1, 2, 3}
set6.add(4)
print(hex(id(set6)), set6) # 0x102e45460 {1, 2, 3, 4}

# remove(x) 从集合中移除x, x不存在则报错
set6.remove(4) #
print(hex(id(set6)), set6) # 0x102e45460 {1, 2, 3}

# 遍历集合
for item in set6:
    print(item)

# update(x) 添加元素，x可以为列表、元组、字符串、字典等可迭代对象
set7 = {1, 2, 3}
set8 = {3, 4, 5}
set7.update(set8) # 必须是可迭代对象，set7.update(6) 是不允许的
print(set7) # {1, 2, 3, 4, 5}

# union(x) 添加元素后返回一个新的集合，x可以为列表、元组、字符串、字典等可迭代对象
set9 = {1, 2, 3}
set10 = {3, 4, 5}
set11 = set9.union(set10)
print(set9) # {1, 2, 3}
print(set11) # {1, 2, 3, 4, 5}

# discard(x) 从集合中移除x，x不存在也不报错
set9.discard(30) # 集合中没有，但不会报错

# pop() 随机取出集合中的一个元素，如果集合为空则报错
print(set9.pop()) # 1
print(set9) # {2, 3}

# clear() 清空集合
set9.clear()
print(set9) # set()

# difference(x1, ...) 求set1和x1的差集，返回一个新的集合
set12 = {1, 2, 3}
set13 = {3, 4, 5}
set14 = set12.difference(set13)
set15 = set13.difference(set12)
print(set14) # {1, 2}
print(set15) # {4, 5}

# difference_update(x1, ...) 求set1和x1的差集，不会返回新的集合
print(set12) # {1, 2, 3}
set12.difference_update(set13) # 直接在原集合中修改
print(set12) # {1, 2}

# intersection(x1, ...) 求set1和x1的交集，返回一个新的集合
set16 = {1, 2, 3}
set17 = {3, 4, 5}
set18 = set16.intersection(set17) # {3}
print(set18)

# intersection_update(x1, ...) 求set1和x1的交集，不会返回新的集合
print(set16) # {1, 2, 3}
set16.intersection_update(set17)  # 直接在原集合中修改
print(set16) # {3}

set19 = {1, 2, 3}
set20 = {3, 4, 5}
# & 交集
print(set19 & set20) # {3}

# ｜ 并集
print(set19 | set20) # {1, 2, 3, 4, 5}

# - 差集
print(set19 - set20) # {1, 2}
print(set20 - set19) # {4, 5}

# isdisjoint(set) 判断两个集合是否没有交集
print(set19.isdisjoint(set20)) # False

# set1.issubset(set2) 判断set1是否是set2的子集
print(set19.issubset(set20)) # False
print({3, 4}.issubset(set20)) # True

# set1.issuperset(set2) 判断set1是否是set2的父集
print(set19.issuperset(set20)) # False
print({1, 2, 3, 4, 5}.issuperset(set20)) # True

# set1.symmetric_difference(set2) 求两个集合中不重复的元素，返回一个新的集合
print(set19.symmetric_difference(set20)) # {1, 2, 4, 5}

# set1.symmetric_difference_update(set2) 求两个集合中不重复的元素，不会返回新的集合
print(set19) # {1, 2, 3}
set19.symmetric_difference_update(set20) # 直接在原集合中修改
print(set19) # {1, 2, 4, 5}

# copy 浅拷贝
set21 = set20.copy()
print(set20, hex(id(set20))) # {3, 4, 5} 0x104e09460
print(set21, hex(id(set21))) # {3, 4, 5} 0x104e091c0