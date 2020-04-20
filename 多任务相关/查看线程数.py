import threading
import time

def test1():
    for i in range(5):
        print("-----test1----%d---" % i )
#如果创建thread时执行的函数运行结束意味着这个子线程结束了

def test2():
    for i in range(5):
        print("-----test2----%d---" % i )


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()
    #启动新线程
    #time.sleep(1)意味着主线程休眠1s，则指向test1的线程先执行
    t2.start()
    while True:
       print(threading.enumerate())
       if len(threading.enumerate())<=1:
            break
       time.sleep(1)
#主线程需要等待子线程结束后才能结束

if __name__ == '__main__':
    main()