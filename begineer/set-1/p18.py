a,b=map(int,input().split())
l=[]
for _ in range(a):
	l.append(input())
for i in range(len(l)):
	if('0' in l[i]):
		l[i]=l[i].replace('0','')
	l[i]=l[i].replace(' ','')
lengths=[]
for i in l:
	if(len(i)>0):
		lengths.append(len(i))
b=min(lengths)
r='1 '*b
r=r.strip()
for i in range(b):
	print(r)
