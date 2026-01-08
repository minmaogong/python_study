"""
    tuple 元组
    不可变 有序
"""

# 创建元组对象
tup1 = (100, 200, 300, 400, 500)
print(tup1, type(tup1)) # (100, 200, 300, 400, 500) <class 'tuple'>

tup2 = (10) # 这里的()是普通的优先级运算符()
print(tup2, type(tup2)) # 10 <class 'int'>

tup3 = (10,) # 如果元组中只有一个元素，需要有,才能识别成是元组
print(tup3, type(tup3)) # (10,) <class 'tuple'>

# 通过推导式的方式创建元组
tup_gen = (i for i in range(1, 101)) # 得到生成器对象
# 将生成器对象封装为一个元组对象
tup4 = tuple(tup_gen)
print(tup4)
