n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(k):
    l=l[len(l)-1:]+l[:len(l)-1]
print(*l)
    
        
    
        
        

    
