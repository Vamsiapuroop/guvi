l=list(input())
j=0
while(j<len(l)):
    temp=l[j]
    l[j]=l[j+1]
    l[j+1]=temp
    j+=2
print("".join(l))
