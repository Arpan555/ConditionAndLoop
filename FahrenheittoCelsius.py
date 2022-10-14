s=int(input())
e=int(input())
w=int(input())
for i in range(s,e+1,w):
    result=((i-32)*5)/9
    print(i,int(result))
