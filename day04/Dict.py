"""
    字典
"""
# 创建字典对象
dict1 = {} # dict1 = dict()
print(type(dict1)) # <class 'dict'>
dict1 = {"name": "张三", "age": 30, "gender": "male"}
print(dict1) # {'name': '张三', 'age': 30, 'gender': 'male'}
dict1 = dict(name = "李四", age = 28, gender = "male")
print(dict1) # {'name': '李四', 'age': 28, 'gender': 'male'}
dict1 = dict([("name", "王五"), ("age", 25), ("gender", "female")]) # 列表 + 元组
print(dict1) # {'name': '王五', 'age': 25, 'gender': 'female'}

# 推导式创建字典
dict2 = {i:i*2 for i in range(10)}
print(dict2) # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}

# 访问元素
print(dict1["name"]) # 王五
# print(dict1["weight"]) # 报错
print(dict1.get("age")) # 25
print(dict1.get("weight")) # None 不会报错，返回None
print(dict1.get("weight", 90)) # 90 没有会返回default

# 添加或者元素
dict1["weight"] = 100
print(dict1)  # {'name': '王五', 'age': 25, 'gender': 'female', 'weight': 100}
dict1["age"] = 26
print(dict1)  # {'name': '王五', 'age': 26, 'gender': 'female', 'weight': 100}

# 成员运算in 只检查key是否在字典中，不会检查value是否在字典中
print("name" in dict1) # True
print("张三" in dict1) # False

# 遍历
# 遍历所有key
for key in dict1.keys():
    print(key, end=" ") # name age gender weight

print()
print("*" * 40)
# 遍历所有value
for value in dict1.values():
    print(value, end=" ") # 王五 26 female 100

print()
print("*" * 40)
# 遍历所有key，value
for key, value in dict1.items():
    print(f"{key}: {value}")

# 删除元素
# del dict1["name"]
# print(dict1) # {'age': 26, 'gender': 'female', 'weight': 100}
# dict1.clear()

# pop(key, default) 获取key对应的value，同时删除该健值对，可设置默认值
# print(dict1.pop("name")) # 王五
# print(dict1) # {'age': 26, 'gender': 'female', 'weight': 100}

# popitem() 取出字典中的最后插入的健值对，字典为空则报错
# print(dict1.popitem()) # ('weight', 100)
# print(dict1) # {'name': '王五', 'age': 26, 'gender': 'female'}

# clear() 清空字典
# dict1.clear()

# dict1.update(dict2) 将dict2中的健值对更新到dict1中
dict3 = {"a": 1, "b": 2, "c": 3}
dict4 = {"d": 4, "e": 5, "f": 6}
dict3.update(dict4)
print(dict3) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# setdefault(key, [, default]) 获取字典中key对应的value，可设置默认值。若key不存在于字典中，将会添加key并将default设为默认值
print(dict3.setdefault("b", 100)) # 2
print(dict3.setdefault("g", 7)) # 7
print(dict3) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}

# copy() 字典
dict5 = dict4.copy()
print(dict4, hex(id(dict4))) # {'d': 4, 'e': 5, 'f': 6} 0x100b31e00
print(dict5, hex(id(dict5))) # {'d': 4, 'e': 5, 'f': 6} 0x100a48ac0

# dict.fromkeys(seq[, default]) 以序列seq中元素做字典的key创建一个新字典，可设置value的默认值
list1 = ["a", "b", "c"]
dict6 = dict.fromkeys(list1)
print(dict6) # {'a': None, 'b': None, 'c': None}
dict6 = dict.fromkeys(list1, 0)
print(dict6)  # {'a': 0, 'b': 0, 'c': 0}
