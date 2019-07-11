n,q=map(int,input().split())
l=list(map(int,input().split()))
for i in range(q):
    a,b=map(int,input().split())
    c=l[a-1:b]
    print(min(c))
    
    
