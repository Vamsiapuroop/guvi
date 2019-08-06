n=input()
m=n.replace(" ","")
c = 0
for i in m:
    if i.isdigit() or i.isalpha():
        pass
    else:
        c+=1
print(c)
        
