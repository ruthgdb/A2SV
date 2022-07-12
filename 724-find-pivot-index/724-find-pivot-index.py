class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        prefSum = [0]
        sums = 0
        
        for i in range(len(nums)):
            sums += nums[i]
            prefSum.append(sums)
        print(prefSum)
        
        for i in range(len(nums)):
            if prefSum[-1] - prefSum[i] == prefSum[i + 1]:
                return i
            
        return -1