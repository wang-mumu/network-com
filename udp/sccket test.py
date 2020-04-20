import socket


def main():
      #创建udp的套接字
      udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
      #端口绑定了就是绑定的端口号，否则发送方的端口号是随机绑定的
      udp_socket.bind(("",7890))
      while True:
            #准备接收方的地址
            #'192.168.1.123'表示目的ip地址
            #8080表示目的端口 是元组
            dest_addr=('192.168.244.1',8080)
            send_data=input("请输入要发送的数据：")
            if send_data == "exit":
                  break
            udp_socket.sendto(send_data.encode("utf-8"),dest_addr)
      #关闭套接字
      udp_socket.close()

if __name__=='__main__':
      main()