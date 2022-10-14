n=int(input())
ev=0
od=0
while n>0:
    r=n%10
    if(r%2==0):
        ev+=r
    else:
        od+=r
    n=n//10
print(ev,od)
