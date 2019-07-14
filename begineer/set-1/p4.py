p,q = map(str,input().split())
m = 0
if len(p)>len(q):
	p,q=q,p
x = 0
while x<len(p):
	  m += (ord(q[x])-ord(p[x]))
	  x += 1
for x in range(x,len(q)):
	  m += ord(q[x])-ord('p')+1
print(m)
