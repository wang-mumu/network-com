# nums = (x*2 for x in range(10))
# print(nums)
# #创建生成器第一种方式 将[]换成(),即生成一个生成器
# for num in nums:
#     print(num)
#调试程序：在函数的上下
#第二种方式：创建函数(生成器的模板)
def create_num(all_num):
    #print("----1----")
    a,b = 0,1
    current_num = 0
    while current_num < all_num:
        #print("----2----")
        #如果函数中有yield语句，那么这个就不再是函数
        #而是一个生成器的模板
        yield a
        #print("----3----")
        #print(a)
        a,b = b,a+b
        current_num += 1
        #print("----4---")
    return "ok...."

#如果再调用create_num的时候，发现这个函数有yield
#那么此时不是调用函数，而是创建一个生成器对象

# obj = create_num(10)
# ret = next(obj)
# print("obj:",ret)
# ret = next(obj)
# print("obj:",ret)


obj2 = create_num(10)
while True:
    try:
        ret = next(obj2)
        print(ret)
    except Exception as ret:
        print(ret.value)
        break

# for num in obj:
#     print(num)