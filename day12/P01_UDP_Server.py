"""
    UDP服务端
"""

# 导包
import socket

# 创建套接字对象
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定ip和端口
udp_socket.bind(('127.0.0.1', 8000))

# 循环
while True:
    # 接收客户端消息
    data, c_addr = udp_socket.recvfrom(1024)

    # 将客户端消息打印到控制台
    print(f"客户端{c_addr[0]}说：{data.decode('utf-8')}")

    # 向客户端发送消息
    udp_socket.sendto("你好，客户端".encode('utf-8'), c_addr)

# 关闭套接字对象
udp_socket.close()