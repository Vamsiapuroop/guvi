n=int(input())
l=list(map(int,input().split()))
v=[]
for i in range(n):
    if i%2==0:
        if l[i]%2!=0:
            v.append(l[i])
    elif i%2!=0:
        if l[i]%2==0:
            v.append(l[i])

for i in v:
    print(i,end=" ")
    
    
    
      
