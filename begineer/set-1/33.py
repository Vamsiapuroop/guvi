n=int(input())
l=list(map(int,input().split()))
z=[]
for i in range(0,n):
    if l[i]==i:
        z.append(i)
        z.sort()

if len(z)>0:
    for x in z:
        print(x,end=" ")
else:
    print("-1")
            
        
    
