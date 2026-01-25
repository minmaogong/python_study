"""
    生成器的返回值
"""
def feibo(n):
    a, b, count = 0, 1, 1
    while count <= n:
        yield b
        a, b, count = b, a + b, count + 1

    return "done" # 抛出异常的信息

# f = feibo(5)
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f)) # StopIteration: done

try:
    f= feibo(10)
    while True:
        print(next(f))
except StopIteration as e:
    print(e)