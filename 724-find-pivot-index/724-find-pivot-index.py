class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefSum = [0]
        sums = 0
        
        for i in range(len(nums)):
            sums += nums[i]
            prefSum.append(sums)
        
        for i in range(len(nums)):
            if prefSum[-1] - prefSum[i] == prefSum[i + 1]:
                return i
            
        return -1