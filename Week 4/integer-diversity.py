from collections import Counter

t = int(input())
for x in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums = [abs(x) for x in nums]
    c = Counter(nums)
    x = 0
    for i in nums:
        if i == 0 and c[i]>0:
            x += 1
            c[i] = 0
        else:
            if c[i] > 1:
                x += 2
                c[i] = 0
            elif c[i] == 1:
                x += 1
                c[i] = 0
    print(x)
