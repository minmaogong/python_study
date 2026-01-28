"""
    通过线程池的方式创建线程
"""
from concurrent.futures.thread import ThreadPoolExecutor


def func(tname):
    global word
    for i, char in enumerate(word):
        word[i] = chr(ord(char) ^ 1)
        print(f"{tname}: {word}\n", end="")
    return word

if __name__ == '__main__':
    word = list("idmmn!vnsme") # 字符串转列表。将不可变的字符串拆分为单个字符组成的列表
    with ThreadPoolExecutor(max_workers=3, thread_name_prefix="线程") as executor:
        future1 = executor.submit(func, "线程1")
        future2 = executor.submit(func, "线程2")
        future3 = executor.submit(func, "线程3")

        # future1.result()
        # future2.result()
        # future3.result()

    print("主线程：", word)

