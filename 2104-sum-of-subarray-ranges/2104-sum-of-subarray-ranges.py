class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total = 0
        
        for i in range(len(nums)):
            minimum = float("inf")
            maximum = float("-inf")
            
            for j in range(i, len(nums)):
                minimum = min(minimum, nums[j])
                maximum = max(maximum, nums[j])
                total += maximum - minimum
                
        return total