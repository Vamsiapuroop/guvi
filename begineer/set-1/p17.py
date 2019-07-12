n,k=map(int,input().split())
li=list(map(int,input().split()))
a=0
for i in range(0,n):
    for j in range(1,n):
        if li[i]+li[j]==k and i!=j:
            a=1
            break
print("yes" if a else "no")
