import socket
import threading

def service_client(new_socket):
    """为客户端返回数据"""
    # 1.接收浏览器发送的请求，即http请求
    # GET / HTTP/1.1
    request = new_socket.recv(1024)
    print(request)

    # 2. 返回http格式的数据给浏览器response
    # 2.1 准备发送给浏览器的数据 --header
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"
    # 2.2 准备发送给浏览器的数据 --body
    response += "<h1>你好呀mumu</h1>"
    new_socket.send(response.encode("gbk"))

    # 3 关闭套接字
    new_socket.close()

def main():
    """用来完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    # 2. 绑定
    tcp_server_socket.bind(("",7890))

    # 3. 变成监听套接字
    tcp_server_socket.listen(128)

    while True:
        # 4.等待新客户端的链接
        new_socket ,client_addr = tcp_server_socket.accept()

        p = threading.Thread(target=service_client,args=(new_socket,))
        p.start()

    #关闭监听套接字
    tcp_server_socket.close()

if __name__ == '__main__':
    main()