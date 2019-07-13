a=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,a-2):
    for j in range(1,a-1):
        for k in range(2,a):
            if l[i]<l[j] and l[j]<l[k]:
                c+=1
print(c)
