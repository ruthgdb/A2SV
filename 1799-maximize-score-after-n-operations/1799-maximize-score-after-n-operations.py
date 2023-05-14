class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort()
        
        @cache
        def dp(arr, i):
            res = 0
            
            for j in range(len(arr)):
                for k in range(j + 1, len(arr)):
                    nums = arr[:j] + arr[j + 1:k] + arr[k + 1:]
                    res = max(res, i * gcd(arr[j], arr[k]) + dp(nums, i + 1))

            return res
        
        return dp(tuple(nums), 1)