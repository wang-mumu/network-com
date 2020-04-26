from gevent import monkey
import gevent
import random
import time

#打补丁（将程序中用到的耗时操作的代码，换成gevent自己实现的模板）
monkey.patch_all()

def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name,i)
        time.sleep(random.random())

gevent.joinall([
    #两个协程
    gevent.spawn(coroutine_work,"work1"),
    gevent.spawn(coroutine_work,"work2"),
])