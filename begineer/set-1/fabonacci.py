n=int(input())
c=0
n1=1
n2=0
l=[]
while c<n:
    nth=n1+n2
    l.append(nth)
    n1=n2
    n2=nth
    c+=1
print(*l)
    
    
