n=int(input())
l=list(map(int,input().split()))
m=[]
for i in range(0,n):
    c=l[i:]
    m.append(sum(c))
print(max(m))
    
