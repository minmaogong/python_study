"""
    列表
    可变 有序
"""
list1 = [100, 200, 300, 400, 500]
print(list1, type(list1)) # <class 'list'>

print(list1[2], list1[-3]) # 300 300

# 切片
print(list1[1:3:1]) # start end step [200, 300] 左开右闭
print(list1[1::1]) # [200, 300, 400, 500] 包含最后一个
print(list1[1::2]) # [200, 400]

# 倒叙
list1.reverse()
print(list1) # [500, 400, 300, 200, 100]

# 复制
list2 = list1[:] # list1.copy()
print(list2) # [500, 400, 300, 200, 100]
print(hex(id(list1)), hex(id(list2))) # 0x100d2c980 0x100e3c5c0

list1.reverse()
# 添加元素
list1.append(600)
print(list1) # [100, 200, 300, 400, 500, 600]
list1.insert(2, 700)
print(list1) # [100, 200, 700, 300, 400, 500, 600]

# 列表相加
list3 = [1, 2, 3]
list4 = ["a", "b", "c"]
list5 = list3 + list4 # 创建新的列表对象
print(list5) # [1, 2, 3, 'a', 'b', 'c']
print(hex(id(list3)), hex(id(list5))) # 0x100d73b00 0x100e3d380

# 列表乘法
print(list3 * 2) # [1, 2, 3, 1, 2, 3]

# 修改
list4[1] = "B"
print(list4) # ['a', 'B', 'c']
list5[3:] = ["A", "B", "C"]
print(list5) # [1, 2, 3, 'A', 'B', 'C']

print(len(list5)) # 6

print(max(list1)) # 700
print(min(list1)) # 100
print(sum(list1)) # 2800

for item in list1:
    print(item, end="\t") # 100	200	700	300	400	500	600

print()
print("*"*50)

for i in range(len(list1)):
    print(list1[i], end="\t") # 100	200	700	300	400	500	600

print()
print("*"*50)

# enumerate 同时获取下标和元素
for i, item in enumerate(list1):
    print(i, item)

# 删除元素
list1.remove(700)
print(list1) # [100, 200, 300, 400, 500, 600]

del list1[2]
print(list1) # [100, 200, 400, 500, 600]

# del  list1 # 删除了列表对象

# 列表嵌套
list6 = [[1, 2], [3, 4], [5, 6]]
for item in list6:
    for num in item:
        print(num, end="\t")
    print()


# *列表推导式
list7 = [1, 2, 3, 4, 5]
list8 = [i * 2 for i in list7]
print(list8) # [2, 4, 6, 8, 10]

list9 = [i for i in range(10) if i % 2 == 0]
print(list9) # [0, 2, 4, 6, 8]

list10 = [100, 200, 300, 300, 300, 400, 500]
list11 = [i for i in list10 if i != 300]
print(list11) # [100, 200, 400, 500]

list12 = [1, 2, 3]
list13 = ["a", "b", "c"]
list14 = [(i, j) for i in list12 for j in list13]
print(list14) # [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]


# zip() 函数 可将多个可迭代对象中对应元素打包为一个个元组
list15 = list(zip(list12, list13))
print(list15) # [(1, 'a'), (2, 'b'), (3, 'c')]
