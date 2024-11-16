n=int(input())
arr=list(map(int,input().split()))
res=[]
res.extend(arr[1:])
res.append(arr[0])
print(*res)
