n=int(input())
A=list(map(int,input().split()))
for i in range(len(A)):
    for j in range(len(A)):
        for k in range(len(A)):
            if i<j<k:
                if A[i]+A[j]==A[k]:
                    print(A[i],A[j],A[k])
