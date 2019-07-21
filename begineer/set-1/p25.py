p=input()
li=list(map(int,input().split()))
maximum=0
i=0
while(i<len(li)-1):
    count=0
    while(i<len(li)-1 and li[i]<li[i+1]):
        count+=1
        i+=1
    if(count>maximum):
        maximum=count
    i+=1
print(maximum+1)
    
