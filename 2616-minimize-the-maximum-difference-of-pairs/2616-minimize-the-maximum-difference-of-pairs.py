import heapq

class Solution:
    def valid_max(self, val, nums, p):
        i = 0
        count = 0
        
        while i < len(nums) - 1:
            if nums[i + 1] - nums[i] <= val:
                i += 1
                count += 1
                
            i += 1

        return count >= p
            
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        left = 0
        right = max(nums) - min(nums)
        best = right
        
        while left <= right:
            mid = (left + right) // 2
            
            if self.valid_max(mid, nums, p):
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return best