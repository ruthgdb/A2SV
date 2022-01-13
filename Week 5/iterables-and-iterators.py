# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

n = int(input())
lis = list(input().split())
k = int(input())
c = 0

outcomes = list(combinations(lis , k))
for outcome in outcomes:
    if('a' in outcome):
        c += 1
print(c / len(outcomes))