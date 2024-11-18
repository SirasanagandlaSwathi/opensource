s=input()
vowels='aeiouAEIOU'
vco=0
cco=0
for i in s:
    if i.isalpha():
        if i in vowels:
            vco+=1
        if i not in vowels:
            cco+=1
print(vco,cco,sep=',')
