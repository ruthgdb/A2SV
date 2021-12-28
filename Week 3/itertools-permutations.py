from itertools import permutations

s, k = input().split()
k = int(k)
s = list(permutations(s,k))
s.sort()
for i in s:
    print("".join(i))

