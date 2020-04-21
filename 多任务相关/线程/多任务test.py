import time
#单任务：总共花了10秒
#多任务：一起执行
import threading

def sing():
    '''唱歌5秒'''
    for i in range(5):
        print("----正在唱：你不配----")
        time.sleep(1)

def dance():
    '''跳舞5秒钟'''
    for i in range(5):
        print("----正在跳：你不配----")
        time.sleep(1)

def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    #启动线程，让线程开始执行
    t2.start()

if __name__ == '__main__':
    main()