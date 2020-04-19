import socket

def main():
    #1.买个手机（创建套接字）
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #2.插上手机卡（绑定本地信息）
    tcp_server_socket.bind(("",7891))

    #3.将手机设置成正常的响铃模式（让默认的套接字由主动变成被动）
    tcp_server_socket.listen(128)
    print('----1----')
    #4.等待别人的电话到来（等待客户端的链接 accept）
    #accept返回元组 左边两个变量，右边一个元组 即元组拆包
    #如果有新的客户端来链接服务器，那么就产生一个新的套接字
    #专门为这个客服端服务
    #client_socket用来为这个客服端服务
    #tcp_server_socket就可以省下来专门等待其他新客服端的链接
    #clientAddr ：客户的地址
    #tcp_server_socket负责监听，client_socket负责通信
    client_socket,clientAddr = tcp_server_socket.accept()
    print('----2----')
    print(clientAddr)
    #服务端先收，客服端先发
    #接收客服端发送过来的请求
    #recv_data是数据
    recv_data = client_socket.recv(1024)

    #回送一部分数据给客户端
    client_socket.send('收到啦我反馈'.encode('gbk'))

    #关闭套接字
    client_socket.close()
    tcp_server_socket.close()
if __name__ == "__main__":
    main()