class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        k = mini = maxx = -1
        res = 0
        
        for i, num in enumerate(nums):
            if not minK <= num <= maxK:
                k = i
            if minK == num:
                mini = i
            if maxK == num:
                maxx = i
                
            start = min(maxx, mini)
            if start > k:
                res += (start - k)
                
        return res