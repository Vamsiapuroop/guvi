d,e=map(str,input().split())
c=0
for q in range(len(d)):
  if d[q]!=e[q]:
    c=c+1
if(c==1):
  print("yes")
else:
  print("no")
