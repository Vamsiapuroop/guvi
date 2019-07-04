m1,m2=map(str,input().split())
if(len(m1)!=len(m2)):
    print("no")
y=[m1.count(j) for j in m1]
z=[m2.count(j) for j in m2]

if(y==z):
    print("yes")
else:
    print("no")
