from itertools import permutations
s=str(input())
r=permutations(s)
for i in r:
    print("".join(i))
