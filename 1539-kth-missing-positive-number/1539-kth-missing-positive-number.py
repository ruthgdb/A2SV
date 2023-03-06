class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr) - 1
        best = -1
        
        while left <= right:
            mid = (left + right) // 2
            missingCount = arr[mid] - mid - 1
            
            if missingCount >= k:
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        
        if best != -1:
            count = arr[best - 1] - best
            return arr[best - 1] + k - count
        
        count = arr[-1] - len(arr)
        return arr[-1] + k - count