"""
    TCP 服务端
"""
import threading

"""
import socket

# 创建 套接字
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
    # 绑定IP和端口
    tcp_socket.bind(('127.0.0.1', 8000))
    # 设置监听
    tcp_socket.listen(100) # 客户端数量
    # 等待客户端连接
    c_socket, c_addr = tcp_socket.accept()
    # 循环
    while True:
        # 接收客户端发送的消息
        data = c_socket.recv(1024)
        # 将客户端消息打印输出到控制台
        if not data:
            break
        # 将客户端消息打印输出到控制台
        print(f"客户端{c_addr[0]}:{c_addr[1]}说：{data.decode('utf-8')}")
        # 向客户端发送消息
        c_socket.send("你好客户端！".encode('utf-8'))
"""

# 优化：可以连接多个客户端 并针对每一个客户端开启新的线程进行处理 + 异常
import socket

# 针对每一个客户端进行处理的函数
def handle_client(c_socket, c_addr):
    try:
    # 循环
        while True:
            # 接收客户端发送的消息
            data = c_socket.recv(1024)
            # 将客户端消息打印输出到控制台
            if not data:
                break
            # 将客户端消息打印输出到控制台
            print(f"客户端{c_addr[0]}:{c_addr[1]}说：{data.decode('utf-8')}")
            # 向客户端发送消息
            c_socket.send("你好客户端！".encode('utf-8'))
    except:
        print(f"和客户端{c_addr[0]}:{c_addr[1]}通信发生了异常")
    finally:
        c_socket.close()

if __name__ == '__main__':
    # 创建 套接字
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
        # 绑定IP和端口
        tcp_socket.bind(('127.0.0.1', 8000))
        # 设置监听
        tcp_socket.listen(100)  # 客户端数量
        while True:
            # 等待客户端连接
            c_socket, c_addr = tcp_socket.accept()
            # 针对每一个客户端开启一个新的线程进行处理
            t = threading.Thread(target=handle_client, args=(c_socket, c_addr))
            t.start()

