a,b=map(str,input().split())
c=0
for q in range(len(a)):
  if a[q]!=b[q]:
    c=c+1
if(c==1):
  print("yes")
else:
  print("no")
