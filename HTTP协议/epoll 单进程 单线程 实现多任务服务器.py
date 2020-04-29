#epoll 套接字在操作系统和应用程序共用的内存空间（内存映射技术）
#以事件通知取代列表
#挨个问 轮询 效率过低 挨个问谁饿
#事件通知 谁饿了谁举手
#单进程 单线程 非堵塞 实现多任务的限制是列表过大，运行起来套接字得一个个复制到
#操作系统来运行，效率不够高
#linux系统才可以用啦

import socket
import re
import select

import socket
import time
import re

def service_client(new_socket,request):
    """为客户端返回数据"""
    # 1.接收浏览器发送的请求，即http请求
    #GET / HTTP/1.1
    # request = new_socket.recv(1024).decode("utf-8")
    # #print(request)
    #将每一行分隔，返回一个包含每行作为元素的列表
    request_lines = request.splitlines()
    #print(request_lines)
    #get post put del
    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)",request_lines[0])
    if ret:
        file_name = ret.group(1)
        print("*"*50,file_name)
        if file_name == "/":
            file_name = "/Bootstrap布局（媒体选择器).html"
    # 2. 返回http格式的数据给浏览器response

    # 2.2 准备发送给浏览器的数据 --body
    try:
        f = open("./website" + file_name, "rb")
    except:
        response = "HTTP.1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "----file not found----"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()

        response_body = html_content

        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"
        response = response_header.encode("utf-8") + response_body

        new_socket.send(response)

    # 3 关闭套接字(把这个加上就是短连接)
    # new_socket.close()

def main():
    """用来完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    # 2. 绑定
    tcp_server_socket.bind(("",7890))

    # 3. 变成监听套接字
    tcp_server_socket.listen(128)

    # 设置套接字为非堵塞的方式
    tcp_server_socket.setblocking(False)

    # 创建一个epoll对象(内存映射空间)
    epl = select.epoll()

    # 将监听套接字对应的fd注册到epoll中（扔套接字对应的文件描述符）
    # select.EPOLLIN检测套接字接收数据
    epl.register(tcp_server_socket.fileno(),select.EPOLLIN)

    client_socket_list = list()

    fd_event_dict = dict()

    while True:
        #epl默认堵塞（原来方式一直轮询浪费资源），直到os监测到数据到来
        #通过事件通知方式告诉这个程序，此时才会解堵塞
        fd_event_list = epl.poll()
        #[（fd,event）],（套接字对应的文件描述符，这个文件描述符对应的是什么事件）]
        #元组拆包
        for fd,event in fd_event_list:
            # 4.等待新客户端的链接
            if fd == tcp_server_socket.fileno():
                new_socket, client_addr = tcp_server_socket.accept()
                epl.register(new_socket.fileno(),select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket

            elif event == select.EPOLLIN:
                #判断已经链接的客户端是否有数据发送过来
                recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
                if recv_data:
                    service_client(fd_event_dict[fd],recv_data)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]
    #关闭监听套接字
    tcp_server_socket.close()

if __name__ == '__main__':
    main()
