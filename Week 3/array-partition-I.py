class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        lis = []
        sum = 0
        for i in range(0,len(nums),2):
            lis.append([nums[i],nums[i+1]])
        for i in range(len(lis)):
            sum += min(lis[i][0], lis[i][1])
        return sum