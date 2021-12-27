n = int(input())
lis = list(map(int, input().split()))
res = all(x > 0 for x in lis) and any(str(x) == str(x)[::-1] for x in lis)
print(res)