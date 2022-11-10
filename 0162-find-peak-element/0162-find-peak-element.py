class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        nums = nums + [float("-inf")]
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            
            if nums[mid - 1] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
                
        return mid 