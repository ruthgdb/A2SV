class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        
        while left < right:
            mid = (right + left) // 2
            
            if mid + 1 < len(arr) - 1 and arr[mid] < arr[mid + 1]:
                left = mid 
            elif mid > 0 and arr[mid - 1] > arr[mid]:
                right = mid 
            else:
                break
            
        return mid