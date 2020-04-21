import threading
import time

class MyThread1(threading.Thread):
    def run(self):
        #对mutexA上锁
        mutexA.acquire()
        #mutexA上锁后延时1秒，等待另外一个线程把mutexB上锁
        print(self.name+"---do1---up---")
        time.sleep(1)
        #此时会堵塞，因为这个mutexB已经被另外的线程抢先上锁了
        mutexB.acquire()
        print(self.name+'---do1---down---')
        mutexB.release()
        mutexA.release()

class MyThread2(threading.Thread):
    def run(self):
        mutexB.acquire()
        # mutexA上锁后延时1秒，等待另外一个线程把mutexB上锁
        print(self.name + "---do2---up---")
        time.sleep(1)
        # 此时会堵塞，因为这个mutexB已经被另外的线程抢先上锁了
        mutexA.acquire()
        print(self.name + '---do2---down---')
        mutexA.release()
        mutexB.release()

mutexA = threading.Lock()
mutexB = threading.Lock()

def main():
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()

#此时出现死锁状态
#类似于男女双方都在等对方道歉