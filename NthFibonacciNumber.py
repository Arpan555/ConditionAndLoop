n=int(input())
a=1
b=1
list=[]
list.append(a)
list.append(b)
for i in range(2,n):
    c=a+b
    a=b
    b=c
    list.append(c)
print(list[-1])
