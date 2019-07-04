a,b=map(int,input().split())
c = 0
for i in range(a,b+1):
   if i>1:
        for x in range(2,i):
            if i%x==0:
                 break
        else:
            c+=1
        
print(c)
        
