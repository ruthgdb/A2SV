n = int(input())
A = set(map(int, input().split()))
m = int(input())
B = set(map(int, input().split()))
newset = set(A.union(B))
print(len(newset))