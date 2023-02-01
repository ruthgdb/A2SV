class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = [(ages[i], scores[i]) for i in range(len(ages))]
        players.sort()
        dp = [0] * len(players)
        maxScore = max(scores)
    
        for i in range(len(players)):
            dp[i] = players[i][1]
            for j in range(i):
                if players[j][1] <= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])
                    maxScore = max(maxScore, dp[i])
                    
        return maxScore