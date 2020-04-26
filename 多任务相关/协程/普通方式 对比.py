#0,1,1,2,3,5,8,13,21,34
a = 0
b = 1
i = 0
fibo = list()
while i<10:
   a,b = b,a+b
   fibo.append(a)
   i += 1

for num in fibo:
    print(num)

#占用空间大