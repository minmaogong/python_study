
# 1. 使用生成式表达式创建一个生成器，生成1到10的偶数。然后使用for循环遍历该生成器，打印每个偶数
print("使用推导式表达式创建生成器")
gen = (x for x in range(1, 11) if x % 2 == 0)
for item in gen:
    print(item)

print("使用生成器函数创建生成器")
def generator1(data):
    for i in data:
        if i % 2 == 0:
            yield i

gen2 = generator1(range(1, 11))
for item in gen2:
    print(item)


print("~" * 50)


# 2.创建一个迭代器类MyIterator, 用于遍历一个给定列表的元素，实现__iter__ 和 __next__方法。使用该迭代器类遍历列表[10, 20, 30, 40]，并打印每个元素
class MyIterator:
    def __init__(self, data):
        self.index = 0
        self.data = data
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        i = self.data[self.index]
        self.index += 1
        return i

mi = MyIterator([10, 20, 30, 40])
for item in mi:
    print(item)