"""
    finally
"""

try:
    res = 10 / 0
    print(res)
except NameError:
    print("发生了异常")
finally:
    # 不管是否发生异常，都会执行的代码
    print("~~~finally~~~")

print("~~~end~~~")

# 面试题
# break continue return

def test_func():
    try:
        for i in range(10):
            if i == 5:
                return
            print(i)
    except:
        print("发生了异常")
    finally:
        print("~~~finally~~~")

test_func()