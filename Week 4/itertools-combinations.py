from itertools import combinations

s, k = input().split()
k = int(k)
s = list(combinations(s,k))
s.sort()
for i in s:
    print("".join(i))