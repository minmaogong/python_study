"""
    通过线程子类创建线程对象
"""
import threading
import time


class WorkerThread(threading.Thread):
    def run(self):
        flag = 0
        while True:
            print(threading.current_thread().name, f"{flag}" * 5)
            flag = flag ^ 1
            time.sleep(0.5)

if __name__ == '__main__':
    thread1 = WorkerThread(name="线程1")
    thread2 = WorkerThread(name="线程2")
    thread1.start()
    thread2.start()

    print("~~~~~~主线程~~~~~~")