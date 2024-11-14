x,y,z=list(map(int,input().split()))
res=z-y
if res<0:
    print(0)
else:
    print(res//x)
