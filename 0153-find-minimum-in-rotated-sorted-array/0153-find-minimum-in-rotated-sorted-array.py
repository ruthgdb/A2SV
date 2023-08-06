class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        best = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[left] <= nums[right]:
                return min(nums[left], nums[best])
            
            if nums[mid] > nums[left]:
                left = mid + 1
            elif nums[mid] == nums[left]:
                return min(nums[left], nums[right], nums[mid])
            else:
                best = mid
                right = mid - 1
                
        return nums[best]