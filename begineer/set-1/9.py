n=int(input())
k=int(input())
sum=0
for m in range(1,n+1):
    sum=sum+m
    if k==m:
        break
print(sum)
