n=int(input())
s=list(map(int,input().split()))
t=[]
for i in range(len(s)):
    m=bin(s[i]).replace("0b"," ")
    t.append(m)
    t.sort(reverse=True)
for j in t:
    print(int(j,2))
           
    

