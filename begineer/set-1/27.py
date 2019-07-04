l=list(input())
j=0
while(j<len(k)):
    temp=k[j]
    k[j]=k[j+1]
    k[j+1]=temp
    j+=2
print("".join(k))
