#模拟服务器
import socket
import re

def service_client(new_socket):
    """为客户端返回数据"""
    # 1.接收浏览器发送的请求，即http请求
    #GET / HTTP/1.1
    request = new_socket.recv(1024).decode("utf-8")
    #print(request)
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
        # 2.1 准备发送给浏览器的数据 --header
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        new_socket.send(response.encode("utf-8"))
        new_socket.send(html_content)

    # 3 关闭套接字
    new_socket.close()

def main():
    """用于完成整体的控制"""
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #设置当服务器先close,即服务器端4次挥手后资源能够立刻释放
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    # 2.绑定本地信息
    tcp_server_socket.bind(("",7892))

    # 3.变成监听套接字
    tcp_server_socket.listen(128)

    while True:
        # 4.等待新客户端的链接
        new_socket,client_addr = tcp_server_socket.accept()

        # 5.为这个客户端服务
        service_client(new_socket)

    tcp_server_socket.close()

if __name__ == '__main__':
    main()