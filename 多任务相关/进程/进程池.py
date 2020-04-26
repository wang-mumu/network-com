from multiprocessing import Pool
import os,time,random

def worker(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%d" % (msg,os.getpid()))
    #random.random()随机生成0到1之间的浮点数
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕，耗时%0.2f" % (t_stop-t_start))

if __name__ == '__main__':
        #定义一个进程池，最大进程数3
        po = Pool(3)
        for i in range(0,10):
            #pool().apply_async(要调用的目标，（传递给目标的参数元组，）)
            #每次循环都将会用空闲出来的子进程去调用目标
            po.apply_async(worker,(i,))

        print("----start-----")
        #关闭进程池，关闭后po不再接收新的请求
        po.close()
        #主进程等待子进程执行完
        po.join()
        print("-----end------")