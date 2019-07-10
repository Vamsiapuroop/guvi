v,a=map(int,input().split())
c=[]
d=0
l=[]
for i in range(v,a+1):
        c.append(bin(i)[2::])
for i in range(0,len(c)):
        l.append(c[i].count("1"))
 
for i in range(0,len(l)):
        if l[i]!=1 and l[i]!=2:
                for p in range(2,l[i]):
                        if l[i]%p==0:
                                break
                if p==l[i]-1:
                        d=d+1
        elif l[i]==2:
                d=d+1
print(d)
