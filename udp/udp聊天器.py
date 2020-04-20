import socket


class CHAT(object):
    def __init__(self):
        pass

    @staticmethod
    def print_menu():
        print("-----聊天器-----")
        print("1:发送信息")
        print("2:接收信息")
        print("0:退出系统")
        num = input("请输入功能对应的序号：")
        return num

    def send_msg(self,udp_socket):
        # 获取对方的ip/port input收获的是字符串
        dest_ip = input("请输入对方的ip:")
        dest_port = int(input("请输入对方的port:"))
        # 从键盘获取数据
        send_data = input("请输入要发送的数据：")
        # 可以使用套接字收发数据
        udp_socket.sendto(send_data.encode("gbk"), (dest_ip, dest_port))

    def recv_msg(self,udp_socket):
        recv_data = udp_socket.recvfrom(1024)
        print("%s:%s" % (str(recv_data[1]),recv_data[0].decode("gbk")))
        print(recv_data[1])

    def run(self):
        # 创建套接字
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 绑定信息
        udp_socket.bind(("",7895))
        while True:
            num = self.print_menu()
            if num == "1":
                # 发数据
                self.send_msg(udp_socket)
            elif num == "2":
                # 收数据
                self.recv_msg(udp_socket)
            elif num == "0":
                # 关闭套接字
                udp_socket.close()
                break
            else:
                print("输入有误请重新输入...")

def main():
        chat = CHAT()
        chat.run()

if __name__=='__main__':
    main()