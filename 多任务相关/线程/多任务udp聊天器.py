import threading
import socket

def recv_msg(udp_socket):
    """接收数据并显示"""
    #接收数据
    while True:
        recv_msg = udp_socket.recvfrom(1024)
        print(recv_msg[0].decode('gbk'))

def send_msg(udp_socket,dest_ip,dest_port):
    """发送数据"""
    while True:
        send_msg = input("输入要发送的数据:")
        udp_socket.sendto(send_msg.encode("gbk"),(dest_ip,dest_port))


def main():
     #创建套接字
     udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
     #绑定信息
     udp_socket.bind(("",7894))
     #获取对方的ip和端口
     dest_ip = input("请输入对方的ip:")
     dest_port = int(input("请输入对方的port:"))
     t_recv = threading.Thread(target=recv_msg,args=(udp_socket,))
     t_send = threading.Thread(target=send_msg,args=(udp_socket,dest_ip,dest_port))

     t_recv.start()
     t_send.start()

if __name__ == '__main__':
    main()