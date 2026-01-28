"""
    通过进程池的方式创建进程对象，这种方式创建出来的进程默认是守护进程，所以需join()确保主进程等待
"""
import multiprocessing
import os
from time import sleep


# 创建10个数字，每次间隔0.5s
def func():
    for i in range(10):
        print(os.getpid(), i)
        sleep(0.5)

if __name__ == "__main__":
    num_process = 5
    pools = multiprocessing.Pool(processes=num_process)

    for _ in range(num_process):
        # pools.apply(func) # 阻塞主进程
        pools.apply_async(func) # 因为是异步的，所以不会阻塞主进程，主进程会继续干自己的活。由于工作进程是守护进程，主进程结束退出后，工作进程也会结束退出，所以如果不做任何处理的情况，工作进程中的任务还没有执行，工作进程就会跟着主进程结束退出了

    pools.close() # 阻止后续任务提交到进程池。当所有任务执行完成后，工作进程会退出
    pools.join() # 阻塞主进程，等待工作进程结束。调用join()前必须先调用close()或者terminate()

    print("~~~~~~end~~~~~~")