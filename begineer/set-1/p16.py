a=int(input())
b=list(map(int,input().split()))
r=[1]*a
for pa in range(a):
    if pa==0:
        if b[pa]>b[pa+1]:
            r[pa]=r[pa]+r[pa+1]
    elif pa>0:
        if b[pa]>b[pa-1]:
            r[pa]=r[pa]+r[pa-1]
print(sum(r))
