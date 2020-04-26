#迭代器：可以记住遍历的位置的对象(具有iter和next方法)
#类创建的实例对象一开始并不能用for

from collections import Iterable
import time

class Classmate(object):
    def __init__(self):
        #列表
        self.names = list()
        self.current_num = 0
    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象称为一个可以迭代的对象，即
        可以使用for,那么必须实现__iter__方法"""
        return self

    def __next__(self):
        #下一次调用保存上一次的值
        if self.current_num < len(self.names):
                ret = self.names[self.current_num]
                self.current_num += 1
                return ret
        else:
            # 抛出异常
            raise StopIteration

#实例对象
classmate = Classmate()
#添加方法
classmate.add("老王")
classmate.add("王二")
classmate.add("李四")

#print("判断classmate是否是可以迭代的对象:",isinstance(classmate,Iterable))
#不加%,当成元组看待
#classmate_iterator = iter(classmate)
#print(next(classmate_iterator))
#print("判断classmate_iterator是否是可以迭代的对象:",isinstance(classmate_iterator,Iterable))
for name in classmate:
    print(name)
    time.sleep(1)

#迭代器比起直接返回列表的方式，占用极小的空间，存储的是生成数据的方式
#迭代器什么时候用，什么时候生成
#列表先生成再用