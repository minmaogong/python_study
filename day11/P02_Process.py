"""
    通过进程类创建进程对象 这种方式创建的进程默认是非守护进程
    同时读写文件
"""
import multiprocessing


# 向文件中写入数据
def write_file():
    print(__name__, "~~~~~~~~~~~~") # __mp_main__~~~~~~~~~~~~
    with open("test.txt", "a", encoding="utf-8") as f: # w 是覆盖 a 是追加
        while True:
            f.write("hello world\n")
            # 将缓冲区数据刷写到文件中
            f.flush()

# 从文件中读取数据
def read_file():
    print(__name__, "~~~~~~~~~~~~") # __mp_main__~~~~~~~~~~~~
    with open("test.txt", "r", encoding="utf-8") as f:
        while True:
            print(f.readline())

# 注意：在Windows中通过multiprocessing.Process创建进程， __name__=="__main__" 必须要加
if __name__ == "__main__":
    # 创建进程
    p1 = multiprocessing.Process(target=write_file)
    p2 = multiprocessing.Process(target=read_file)

    # 启动进程
    p1.start()
    p2.start()