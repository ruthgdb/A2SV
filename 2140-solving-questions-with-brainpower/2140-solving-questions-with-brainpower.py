class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        
        for i in range(n - 1, -1, -1):
            point, jump = questions[i]
            pick_curr = point + dp[i + jump + 1] if i + jump + 1 < n else point
            not_pick = dp[i + 1] if i + 1 < n else 0
            dp[i] = max(pick_curr, not_pick)
         
        return dp[0]