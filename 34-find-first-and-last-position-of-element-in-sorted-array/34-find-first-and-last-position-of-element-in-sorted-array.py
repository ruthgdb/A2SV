class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first, last, left, right = -1, -1, 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                first = mid
                right = mid - 1
                
        if first == -1:
            return [-1, -1]
        
        left, right = first, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                last = mid
                left = mid + 1
                
        return [first, last]