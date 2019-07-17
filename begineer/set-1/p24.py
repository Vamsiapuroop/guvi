from itertools import combinations as p
k=int(input())
p=pow(2,k)
for i in range(p):  
    m=bin(i).replace("0b","")
    print(m.zfill(k))

