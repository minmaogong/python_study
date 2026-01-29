"""
    TCP客户端
"""
import socket

# 创建套接字对象
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
    # 连接服务器
    server_addr = ("127.0.0.1", 8000)
    tcp_socket.connect(server_addr)
    # 循环
    while True:
        # 向服务器发送消息
        msg = input("客户端说：")
        if not msg:
            msg = "None"
        tcp_socket.send(msg.encode('utf-8'))
        # 接收服务器返回的消息
        data = tcp_socket.recv(1024)
        # 将服务器返回的消息打印到控制台
        print(f"服务器说：{data.decode('utf-8')}")
    # 关闭套接字对象
