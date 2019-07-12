t= int(input())
b =[]
for i in range(0,t):
  l= list(map(int,input().split()))
  b.append(l)
merge = []
for i in b:
  merge = merge + i
c = sorted(merge)
for i in c:
  print(i,end = " ")
