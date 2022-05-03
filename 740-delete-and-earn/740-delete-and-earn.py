class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        n = max(nums) + 1
        
        value = [0] * n

        for num in nums:
            value[num] += num
                  
        dp = [0] * n
        dp[0] = value[0]
        dp[1] = max(value[0], value[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + value[i])
            
        return max(dp[-1], dp[-2])