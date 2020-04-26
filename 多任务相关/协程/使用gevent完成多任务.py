import gevent
from gevent import monkey
import time

#把耗时的代码换成gevent的耗时操作
monkey.patch_all()
#遇到延时操作就可以切换任务(gevent.sleep)
def f(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        #gevent.sleep(0.3)
        time.sleep(0.3)

print("---1----")
g1 = gevent.spawn(f,5)
print("---2----")
g2 = gevent.spawn(f,5)
print("---3----")
g3 = gevent.spawn(f,5)
print("---4----")

# g1.join()
# g2.join()
# g3.join()
gevent.joinall([g1,g2,g3])

#进程是资源分配的单位，线程执行任务，协程依赖于线程
