class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefSum = [0]
        left = 0
        sums = 0
        
        for i in range(len(nums)):
            sums += nums[i]
            prefSum.append(sums)
            
        while left < len(nums):
            if prefSum[left] == prefSum[len(nums)] - prefSum[left + 1]:
                return left
            else:
                left += 1
        
        return -1
            