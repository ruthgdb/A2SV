class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = [(ages[i], scores[i]) for i in range(len(ages))]
        players.sort()
        arr = [0] * len(players)
    
        for i in range(len(scores)):
            arr[i] = players[i][1]
            for j in range(i):
                if players[j][1] <= players[i][1]:
                    arr[i] = max(arr[i], arr[j] + players[i][1])
                    
        return max(arr)