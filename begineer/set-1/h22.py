n=int(input())
lt=list(map(int,input().split()))
r=1
l=[]
for i in lt:
  r=r*i
for i in lt:
  l.append(r//i)
print(*l)
    
    


