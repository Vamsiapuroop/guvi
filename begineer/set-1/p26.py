n=input()
li=list(map(int,input().split()))
a=1
for i in range(0,len(li)-1):
    if li[i]<li[i+1]:
        a+=1
print(a)
        
        
