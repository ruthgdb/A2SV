class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefSum = nums
        
        for i in range(1, len(nums)):
            prefSum[i] += prefSum[i - 1]
            
        return prefSum