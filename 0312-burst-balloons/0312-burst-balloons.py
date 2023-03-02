class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        
        @cache
        def dp(i, j):
            if i > j:
                return 0
            
            answer = 0
            
            for k in range(i, j + 1):
                answer = max(answer, dp(i, k - 1) + nums[i - 1] * nums[k] * nums[j + 1] + dp(k + 1, j))
                
            return answer
                
        return dp(1, len(nums) - 2)