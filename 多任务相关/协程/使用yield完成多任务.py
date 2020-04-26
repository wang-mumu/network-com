import  time

def task_1():
    while True:
        print("----1----")
        time.sleep(0.1)
        yield

def task_2():
    while True:
        print("---2---")
        time.sleep(0.1)
        yield

def main():
    t1 = task_1()
    t2 = task_2()
    #死循环
    while True:
        next(t1)
        next(t2)

if __name__ == '__main__':
    main()

#并发：假的多任务
#协程实现多任务浪费资源最小，调用任务切换任务需要资源最小