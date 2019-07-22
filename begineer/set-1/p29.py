num = int(input())
nby2 = int(num/2)
l = []
for i in range(nby2,num):
    s = i+sum(map(int,list(str(i))))
    if s == num:
        print(1)
        print(i)
        break
else:
    print(0)
