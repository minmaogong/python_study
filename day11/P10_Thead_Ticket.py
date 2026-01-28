"""
    线程安全问题案例
"""
import threading
import time


def sale_ticket():
    global ticket_num

    while True:
        # 加锁
        lock.acquire()
        if ticket_num <= 0:
            # 释放锁
            lock.release()
            break

        time.sleep(0.1)
        ticket_num -= 1
        # 释放锁
        lock.release()
        print(f"{threading.current_thread().name}卖了1张票，还剩{ticket_num}张")

if __name__ == "__main__":
    ticket_num = 100
    # 创建锁
    lock = threading.Lock()
    threads = [threading.Thread(target=sale_ticket, name="窗口" + str(i+1)) for i in range(3)]
    [t.start() for t in threads]
    [t.join() for t in threads]
