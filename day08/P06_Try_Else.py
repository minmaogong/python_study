"""
    try except else
"""
try:
    res = 1 / 0
except:
    print("发生了异常")
else:
    # 如果try中代码没有发生异常，将执行else中的代码
    # 将不发生异常执行的代码放到else中，有助于代码的可读性和可维护性
    print(res)

print("~~~end~~~")