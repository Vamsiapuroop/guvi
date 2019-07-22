rlen,r=map(int,input().split())
if rlen<r:
    rlen,r=r,rlen
l=[]
for m in range(r):
    temp=list(map(int,input().split()))
    temp.sort()
    l.append(temp)

for i in range(rlen):
    t=[]
    for j in range(r):
        t.append(l[j][i])
    t.sort()
    for j in range(r):
        l[j][i]=t[j]
for i in range(r):
    print(*l[i])
    
    
   
    
