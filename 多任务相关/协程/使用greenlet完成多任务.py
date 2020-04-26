from greenlet import greenlet
import time
#greenlet对yield进行了封装
def test1():
    while True:
        print("---1---")
        gr2.switch()
        time.sleep(0.3)

def test2():
    while True:
        print("--2---")
        gr1.switch()
        time.sleep(0.3)

gr1 = greenlet(test1)
gr2 = greenlet(test2)

#切换到gr1中执行
gr1.switch()