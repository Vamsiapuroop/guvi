a=int(input(""))
n=list(map(int,input().split()))
large=max(n)
y,z=0,0
for i in range(0,len(n)):
 for j in range(i+1,len(n)):
  if abs(n[i]+n[j])< large:
   y,z=n[i],n[j]
   large=abs(y+z)
print(y, z)
