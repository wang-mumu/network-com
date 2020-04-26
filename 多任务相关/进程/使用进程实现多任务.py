import multiprocessing
import time
#进程完成多任务耗费的资源比较大
def test1():
    while True:
        print("1---------")
        time.sleep(1)

def test2():
    while True:
        print("2--------")
        time.sleep(1)

def main():
    #process类
    t1 = multiprocessing.Process(target=test1)
    t2 = multiprocessing.Process(target=test2)
    #创建一个新的进程 代码+用到的资源
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()