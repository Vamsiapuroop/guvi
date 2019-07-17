k=int(input())
p=pow(2,k)
l=[]
for i in range(p):  
    m=bin(i).replace("0b","")
    l.append(m.zfill(k))
    l.sort(key=(lambda x:x.count('1')))
for i in l:
    print(i)

