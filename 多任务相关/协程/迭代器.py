#迭代器：可以记住遍历的位置的对象
#类创建的实例对象一开始并不能用for

from collections import Iterable
import time

class Classmate(object):
    def __init__(self):
        #列表
        self.names = list()

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象称为一个可以迭代的对象，即
        可以使用for,那么必须实现__iter__方法"""
        return ClassIterator(self)
        #返回迭代器对象
        #自己的引用给你一份

#迭代器（取值）
class ClassIterator(object):
    def __init__(self,obj):
        self.obj = obj
        self.current_num = 0
    def __iter__(self):
        pass
    def __next__(self):
        #下一次调用保存上一次的值
        if self.current_num < len(self.obj.names):
                ret = self.obj.names[self.current_num]
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
