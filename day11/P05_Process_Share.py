"""
    进程之间数据的共享
"""
import multiprocessing
import os
import random
import time

"""
# 默认情况下，进程之间内存隔离，数据不能共享
# 向list1中追加10个元素
def func(list1):
    for i in range(10):
        list1.append(i)
        print(os.getpid(), list1, id(list1))

if __name__ == '__main__':
    list1 = []
    p1 = multiprocessing.Process(target=func, args=(list1,))
    p2 = multiprocessing.Process(target=func, args=(list1,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("主进程：", list1, id(list1))
"""

# 通过Queue实现进程之间数据的共享

# 间隔随机时间向queue中放入随机数
def func1(queue):
    while True:
        random_num = random.randint(1, 50)
        queue.put(random_num)
        print(f"进程{os.getpid()}向队列中放入了元素{random_num}")
        time.sleep(0.1)

# 从queue中取出数据
def func2(queue):
    while True:
        num = queue.get()
        print(f"进程{os.getpid()}从队列中取出了元素{num}")
        time.sleep(0.1)

if __name__ == '__main__':
    # queue = multiprocessing.Queue()
    # p1 = multiprocessing.Process(target=func1, args=(queue,))
    # p2 = multiprocessing.Process(target=func2, args=(queue,))
    #
    # p1.start()
    # p2.start()
    #
    # p1.join()
    # p2.join()

    queue = multiprocessing.Manager().Queue()
    pools = multiprocessing.Pool(processes=2)
    pools.apply_async(func1, args=(queue,))
    pools.apply_async(func2, args=(queue,))
    pools.close()
    pools.join()