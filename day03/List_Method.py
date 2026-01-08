"""
    list中的函数
"""
list1 = [100, 200, 300, 400, 500]
list1.insert(0, 30)
print(list1) # [30, 100, 200, 300, 400, 500]
list1.append(600)
print(list1) # [30, 100, 200, 300, 400, 500, 600]
list1.extend([700, 800])
print(list1) # [30, 100, 200, 300, 400, 500, 600, 700, 800]
del list1[6:] # 删除指定位置的数据或切片
print(list1) # [30, 100, 200, 300, 400, 500]
list1.remove(30) # 删除第一次出现的x
print(list1) # [100, 200, 300, 400, 500]
list1.pop(3) # 删除指定位置的数据，默认为末尾数据
print(list1) # [100, 200, 300, 500]
list1.clear()
print(list1) # []
list1[0:5] = [44, 22, 11 ,55, 33]
print(list1) # [44, 22, 11, 55, 33]

print(sorted(list1)) # [11, 22, 33, 44, 55]
print(sorted(list1, reverse=True)) # [55, 44, 33, 22, 11]
print(list1) # [44, 22, 11, 55, 33]
list1.sort()
print(list1) # [11, 22, 33, 44, 55]
list1.sort(reverse=True)
print(list1) # [55, 44, 33, 22, 11]
list1.reverse()
print(list1) # [11, 22, 33, 44, 55]
print(list1.index(33)) # 2
list1.append(33)
print(list1) # [11, 22, 33, 44, 55, 33]
print(list1.index(33, 3)) # 5
print(list1.count(33)) # 2
print(len(list1)) # 6
list2 = list1.copy()
print(list2) # [11, 22, 33, 44, 55, 33]

aa = range(10)
print(type(aa)) # <class 'range'>

# list(x) 将序列转换为列表
bb = list(aa)
print(bb, type(bb)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] <class 'list'>
