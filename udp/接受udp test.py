from socket import *

def main():
        #1.创建套接字
        udp_socket = socket(AF_INET,SOCK_DGRAM)
        #2.绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
        local_addr = ("", 7888)
        udp_socket.bind(local_addr)
        while True:
                #3.等待接受双方发送的数据
                #1024最大字节
                recv_data=udp_socket.recvfrom(1024)
                #recv_data是元组（接受的数据，发送方的ip,端口）
                print(recv_data[0].decode('gbk'))
        #关闭套接字
        udp_socket.close()

if __name__== "__main__":
    main()