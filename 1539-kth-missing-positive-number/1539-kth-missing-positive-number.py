class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i, num in enumerate(arr): 
            if num - i - 1 >= k:
                count = arr[i - 1] - i
                return arr[i - 1] + k - count
            
        count = arr[-1] - len(arr)
        return arr[-1] + k - count