n=int(input())
arr=list(map(int,input().split()))
s1=0
ma=0
for i in range(n):
    s1+=arr[i]
    ma=max(s1,ma)
print(ma)
