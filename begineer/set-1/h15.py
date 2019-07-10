a=int(input())
b=list(map(int,input().split(" ")))
r=max(b)
s=[]
for i in range(0,len(b)):
         t=b[i:]
         q=max(t)
         if(b[i]==q):
              s.append(b[i])
print(*s)
print(r)
