st=str(input())
mx=""
if mx<st:
    for i in range(len(st)):
        mx=max(mx,st[i:])
    print(mx)
    

