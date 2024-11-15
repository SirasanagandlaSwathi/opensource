import math
x,n=list(map(int,input().split()))
res=x*100
if res>=n:
    print(0)
else:
    resu=n-res
    ap=math.ceil(resu/100)
    print(ap)
