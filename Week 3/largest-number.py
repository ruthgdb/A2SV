class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return str(0)
        lis = list(map(str, nums))
        for _ in range(len(lis)):
            for i in range(len(lis)):
                if i < (len(lis) - 1) and lis[i]+lis[i+1] < lis[i+1]+lis[i]:
                    lis[i],lis[i+1] =  lis[i+1],lis[i]
        return ''.join(lis)
        