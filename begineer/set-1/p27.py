AA,BB=map(int,input().split())
CC1=list(map(int,input().split()))
p=list(map(int,input().split()))
q=[]
aa=0
for i in range(AA):
    x=p[i]/CC1[i]
    q.append(x)
while BB>=0 and len(q)>0:
    mindex=q.index(max(q))
    if BB>=CC1[mindex]:
        aa=aa+p[mindex]
        BB=BB-CC1[mindex]
    CC1.pop(mindex)
    p.pop(mindex)
    q.pop(mindex)
print(aa)
