import math
n,q=map(int,input().split())
li=list(map(int,input().split()))
b=[]
for i in range(0,q):
    l,r=map(int,input().split())
    b.append([l,r])
for j in b:
    d=j[0]-1
    e=j[1]-1
    print(math.gcd(li[d],li[e]))
