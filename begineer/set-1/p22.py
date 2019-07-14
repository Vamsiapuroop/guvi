a=int(input())
s=list(map(int,input().split()))
su=0
se=0
for i in range(a):
	if i%2==0:
		su=su+s[i]
	else:
		se+=s[i]
print(max(su,se))
