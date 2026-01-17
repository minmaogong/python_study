"""
    Lambda 表达式
"""

"""
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

# 函数可以作为参数进行传递
def calculate(a, b, op):
    return op(a, b)


print(calculate(3, 5, add))
"""

# 使用lambda匿名函数
def calculate(a, b, op):
    return op(a, b)


print(calculate(10, 20, lambda a, b: a + b))


list1 = [10, 20, 30, 40]

# 推导式
list2 = ["atguigu" + str(i) for i in list1]
print(list2)


#
def my_map(list3, func):
    list4 = []
    for i in list3:
        list4.append(func(i))
    return list4


print(my_map([10, 20, 30, 40], lambda a: a * 2)) # [20, 40, 60, 80]

print(list(map(lambda item: item * 2, [100, 200, 300, 400]))) # [200, 400, 600, 800]

student_list = [{"name": "zhang3", "age": 36}, {"name": "li4", "age": 14}, {"name": "wang5", "age": 27}]

print(sorted(student_list, key=lambda x: x["age"])) # [{'name': 'li4', 'age': 14}, {'name': 'wang5', 'age': 27}, {'name': 'zhang3', 'age': 36}]

filter_result = filter(lambda x: x > 0, [-1, -3, 0, 7, 9])
print(list(filter_result)) # [7, 9]



def dog(name:str, age:(1, 99), species:'狗狗的品种') -> tuple:
    return name, age, species

print(dog.__annotations__) # {'name': <class 'str'>, 'age': (1, 99), 'species': '狗狗的品种', 'return': <class 'tuple'>}