t=int(input())
for i in range(t):
    m,n=list(map(int,input().split()))
    if(n==0):
        print(0)
    else:
        rem=m//10
        print(rem*n)
