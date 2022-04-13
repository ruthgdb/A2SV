class Solution:
    def check(self, nums: List[int]) -> bool:
        k = len(nums) - 1
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                k = i
        k += 1
        temp = nums[:k]
        nums = nums[k:]
        
        nums = nums + temp
        
        return nums == sorted(nums)