n, m = input().split()
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
count = 0

for x in A:
    if x in arr: count += 1
for x in B:
    if x in arr: count -= 1
print(count)
