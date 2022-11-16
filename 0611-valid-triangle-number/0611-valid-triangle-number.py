class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        valid_triplets = 0
        nums.sort()
        
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums)):
                total = nums[i] + nums[j]
                k = bisect.bisect_left(nums, total)
                valid_triplets += max(0, k - j - 1)
                
        return valid_triplets