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
        
        count = arr[best - 1] - best if best != -1 else arr[-1] - len(arr)
        best = 0 if best == -1 else best
        return arr[best - 1] + k - count