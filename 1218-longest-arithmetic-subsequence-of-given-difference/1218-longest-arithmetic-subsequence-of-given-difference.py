class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        max_sequence = 1
        
        for num in arr:
            if num - difference in dp:
                dp[num] = dp[num - difference] + 1
                max_sequence = max(max_sequence, dp[num])
            else:
                dp[num] = 1
                
        return max_sequence