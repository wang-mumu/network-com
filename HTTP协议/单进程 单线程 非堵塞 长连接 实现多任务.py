#用单进程，单线程实现多任务
#核心方法：将套接字设置为非堵塞的方式 非堵塞会有异常
#效率随着列表的变大越来越低 所以要把服务完的套接字从列表中踢出去
#长连接：减少服务器压力，减少资源

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

    client_socket_list = list()

    # 设置套接字为非堵塞的方式
    tcp_server_socket.setblocking(False)
    while True:
        #增加延时看效果
        time.sleep(0.5)

        # 4.等待新客户端的链接
        try:
           new_socket ,client_addr = tcp_server_socket.accept()
        except Exception as ret:
            print("---没有新的客户端到来----")
        else:
            print("---只有没有产生异常，意味着，来了一个新的客户端")
            #设置套接字为非堵塞的方式
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)

        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024).decode("utf-8")
            except Exception as ret:
                print("---这个客户端没有发送数据---")
            else:
                if recv_data:
                   print(("---客户端发送过来数据"))
                   service_client(client_socket,recv_data)
                else:
                    #对象调用close导致了recv返回
                    client_socket_list.remove(client_socket)
                    client_socket.close()
                    print("---客户端已经关闭-----")

    #关闭监听套接字
    tcp_server_socket.close()

if __name__ == '__main__':
    main()