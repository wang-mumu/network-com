#全局变量指向没有改箭头，则不用加global
import threading
import time
#定义一个全局变量
g_nums = [11,12]
g_num = 12

def test1(temp):
    temp.append(33)
    print("---in test1 temp=%s----" % str(temp) )

def test2(temp):
    print("----in test2 temp=%s----" % str(temp))

def main():
    #target指定将来新线程去哪个函数执行代码
    #args是调用函数，传的数据
    t1 = threading.Thread(target=test1,args=(g_nums,))
    t2 = threading.Thread(target=test2,args=(g_num,))
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    print("----in main Thread g_num = %d----" % g_num)

if __name__ == '__main__':
    main()