string=input()
l=[]
for i in string:
    l.append(int(i))
li=[]
for x in l:
    x=x*x
    li.append(x)
print(sum(li))

    
