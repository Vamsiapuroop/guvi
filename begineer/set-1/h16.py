a,b=map(int,input().split(" "))
l=list(map(int,input().split(" ")))
r=[[abs(i-b),i]for i in l]
r=sorted(r)
r=r[1:]
r=[i[1] for i in r[ :3]]
print(*r)
