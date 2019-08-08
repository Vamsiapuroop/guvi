num=int(input())
l=input()
l=l[::-1]
for i in l:
    if i in "aeiouAEIOU":
        l=l.replace(i,"")
print(l)
      
