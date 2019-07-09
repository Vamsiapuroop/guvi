    
from itertools import combinations
num ,x = input().split()
x = int(x)
snum = []
comb = combinations(num,len(num)-x)
for i in comb:
    snum.append("".join(i))
print(min(snum))
