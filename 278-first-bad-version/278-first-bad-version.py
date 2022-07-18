# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first, left, right = n, 0, n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                first = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return first