"""
     UDP客户端
"""

# 导包
import socket

# 创建套接字对象
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
    while True:
        server_addr = ('127.0.0.1', 8000)
        msg = input("客户端说：")
        udp_socket.sendto(msg.encode('utf-8'), server_addr)

        data, s_addr = udp_socket.recvfrom(1024)

        print(f"服务器说：{data.decode('utf-8')}")
