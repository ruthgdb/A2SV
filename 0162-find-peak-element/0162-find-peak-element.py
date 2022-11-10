class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 1
        right = len(nums)
        nums = [float("-inf")] + nums + [float("-inf")]
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                break
            
            if nums[mid - 1] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
                
        return mid - 1