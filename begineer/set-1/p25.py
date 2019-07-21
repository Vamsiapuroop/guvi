n=input()
li=list(map(int,input().split()))
x=0
a=1
for i in li:
    if x<len(li)-1 and li[i]<li[i+1]:
        a+=1
print(a)
    
