n,k=map(int,input().split())
l=[]
for i in range(n):
    z=set(map(int,input().split()))
    l.append(z)
num=z.intersection(*l)
print(*num)
    
    
    

    
