"""
    深拷贝和浅拷贝
"""
import copy

"""
# 浅拷贝
list1 = [1,2,3,[100,200,300]]

print(id(list1), id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3]), list1)

list2 = copy.copy(list1) # 浅拷贝

print(id(list2), id(list2[0]), id(list2[1]), id(list2[2]), id(list2[3]), list2)

print("~"*50)
list1[0] = 100 # 不可变
print(id(list1), id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3]), list1)
print(id(list2), id(list2[0]), id(list2[1]), id(list2[2]), id(list2[3]), list2)

print("~"*50)
list1[3].append(400) # 可变
print(id(list1), id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3]), list1)
print(id(list2), id(list2[0]), id(list2[1]), id(list2[2]), id(list2[3]), list2)
"""

"""
# 深拷贝
list1 = [1,2,3,[100,200,300]]
print(id(list1), id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3]), list1)
list2 = copy.deepcopy(list1) # 深拷贝
print(id(list2), id(list2[0]), id(list2[1]), id(list2[2]), id(list2[3]), list2)

print("~"*50)

list1[0] = 100
print(id(list1), id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3]), list1)
print(id(list2), id(list2[0]), id(list2[1]), id(list2[2]), id(list2[3]), list2)

print("~"*50)

list1[3].append(400)
print(id(list1), id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3]), list1)
print(id(list2), id(list2[0]), id(list2[1]), id(list2[2]), id(list2[3]), list2)
"""


# 拷贝的特殊情况
# 1. 非容器类型（如数字，字符串、和其他“原子”类型的对象）无法拷贝
import copy

var1 = 1
print(id(var1), var1) # 4334887928 1

var2 = copy.copy(var1)
print(id(var2), var2) # 4334887928 1

var3 = copy.deepcopy(var1)
print(id(var3), var3) # 4334887928 1

# 2.元组变量如果只包含原子类型对象，则不能对其深拷贝
tuple1 = (1,2,3)
print(id(tuple1), tuple1)

tuple2 = copy.deepcopy(tuple1)
print(id(tuple2), tuple2)

tuple1 = (1,2,3,[])
print(id(tuple1), tuple1)

tuple2 = copy.deepcopy(tuple1)
print(id(tuple2), tuple2) 