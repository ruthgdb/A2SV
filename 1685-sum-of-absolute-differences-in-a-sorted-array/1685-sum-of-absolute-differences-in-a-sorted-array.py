class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefSum = [nums[0]]
        postSum = [nums[-1]]
        res = []
        
        for i in range(1, n):
            prefSum.append(nums[i] + prefSum[-1])
            
        for i in range(n - 2, -1, -1):
            postSum.append(nums[i] + postSum[-1])
            
        postSum.reverse()
        
        for i in range(n):
            left = abs((i * nums[i]) - (prefSum[i] - nums[i]))
            right = abs(((n - 1 - i) * nums[i]) - (postSum[i] - nums[i]))
            res.append(left + right)
            
        return res