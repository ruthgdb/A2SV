nums = list(map(int, input().split()))
n = len(nums)
c = 0
for i in nums:
    if i == 0:
        nums.remove(i)
        c += 1
for i in range(c):
    nums.append(0)
print(nums)