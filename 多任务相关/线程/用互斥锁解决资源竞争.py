#线程同步能够保证多个线程安全访问竞争资源，最简单的同步机制是引入互斥锁
import threading
import time

#定义一个全局变量
g_num = 0

def test1(num):
    global g_num
    #上锁，如果之前没有被上锁，那么此刻上锁成功
    #如果上锁之前已经被上锁了，那么此刻会堵塞在这里，直到这个
    #锁被解开位置
    for i in range(num):
        mutex.acquire()
        g_num += 1
        #解锁
        mutex.release()
    print("----in test1 g_num=%d----" % g_num )

def test2(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("----in test2 g_num=%d----" % g_num)

#创建一个互斥锁，默认是没有上锁的
mutex = threading.Lock()

def main():
    t1 = threading.Thread(target=test1,args=(1000000,))
    t2 = threading.Thread(target=test2,args=(1000000,))
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()
