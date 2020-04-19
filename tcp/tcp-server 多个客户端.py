import socket

def main():
    #1.买个手机（创建套接字）
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #2.插上手机卡（绑定本地信息）
    tcp_server_socket.bind(("",7891))

    #3.将手机设置成正常的响铃模式（让默认的套接字由主动变成被动）
    tcp_server_socket.listen(128)
    #4.等待别人的电话到来（等待客户端的链接 accept）
    #accept返回元组 左边两个变量，右边一个元组 即元组拆包
    #如果有新的客户端来链接服务器，那么就产生一个新的套接字
    #专门为这个客服端服务
    #client_socket用来为这个客服端服务
    #tcp_server_socket就可以省下来专门等待其他新客服端的链接
    #clientAddr ：客户的地址
    #tcp_server_socket负责监听，client_socket负责通信
    #第一个while true是循环等待不同客服端
    #第二个while true是为一个顾客服务
    while True:
            print('----等待一个新的客服端到来----')
            client_socket,clientAddr = tcp_server_socket.accept()
            print('----一个新的客服端已经到来%s----' % str(clientAddr))
            while True:
                    #服务端先收，客服端先发
                    #接收客服端发送过来的请求
                    #recv_data是数据
                    #recv默认会堵塞
                    recv_data = client_socket.recv(1024)
                    print("客服端收到的请求是：%s" % recv_data.decode("gbk"))
                    #如果recv解堵塞，那么有两种方式：
                    #1.客户端发送过来数据
                    #2.客户端调用close导致
                    if recv_data:
                            #回送一部分数据给客户端
                            client_socket.send('服务端已处理'.encode('gbk'))
                    #if如果是none和false不成立 以及数据为空
                    else:
                        break
            #关闭套接字
            client_socket.close()
            print("已经为此客户服务完毕")

    tcp_server_socket.close()

if __name__ == "__main__":
    main()