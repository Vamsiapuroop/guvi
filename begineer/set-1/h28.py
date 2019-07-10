n=int(input())
l=list(map(int,input().split()))
for i in range(0,n):
    c=l[i:]
    print(sum(c))
    break
