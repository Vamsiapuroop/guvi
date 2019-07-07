n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)-1):
    if l[i]+l[i+1]==0 or l[i]+l[i+1]==-1 or l[i]+l[i+1]==1:
        print(l[i],end=" ")
