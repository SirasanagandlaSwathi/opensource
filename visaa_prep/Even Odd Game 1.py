n=int(input())
res=0
while(n>0):
    rem=n%10
    res=res+rem
    n=n//10
if(res%2==0):
    print("Vignesh")
else:
    print("Charan")
    
