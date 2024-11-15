n=int(input())
arr=list(map(int,input().split()))
res=sorted(arr)
if(res==arr):
    print('true')
else:
    print('false')
