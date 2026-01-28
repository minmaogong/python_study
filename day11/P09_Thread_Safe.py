"""
    线程安全问题
        多个线程对同一个数据进行修改操作，可能会出现数据不一致的问题

    互斥锁
        保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确性
"""
"""
# 线程不安全情况
import threading
import time


def func():
    global g_num
    for i in range(10):
        # g_num += 1 ==> g_num = g_gum + 1 ==>
        temp = g_num + 1
        time.sleep(0.1)
        g_num = temp
        print(f"当前线程{threading.current_thread().name}---->${g_num}")

if __name__ == '__main__':
    g_num = 0
    threadList = [threading.Thread(target=func, name="线程" + str(i)) for i in range(3)]
    [t.start() for t in threadList]

    print(f"主线程：{g_num}")
"""

# 加锁解决线程安全问题
import threading
import time


def func():
    global g_num
    for i in range(10):
        # 加锁
        lock.acquire()

        # g_num += 1 ==> g_num = g_gum + 1 ==>
        temp = g_num + 1
        time.sleep(0.1)
        g_num = temp

        # 释放锁
        lock.release()
        print(f"当前线程{threading.current_thread().name}---->${g_num}")

if __name__ == '__main__':
    g_num = 0
    # 创建锁对象
    lock = threading.Lock()
    threadList = [threading.Thread(target=func, name="线程" + str(i)) for i in range(3)]
    [t.start() for t in threadList]

    print(f"主线程：{g_num}")