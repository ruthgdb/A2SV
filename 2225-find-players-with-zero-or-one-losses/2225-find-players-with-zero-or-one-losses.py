class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        """
        players:
            -1: havent played a game
             >= 0: number of matches lost

        """
        maxNum = max([max(winner, loser) for winner, loser in matches])
        answer = [[], []]
        
        # -1 cause no players have played yet
        players = [-1] * (maxNum + 1)
        
        for winner, loser in matches:
            # if winner or loser havent played yet, start with 0
            if players[winner] == -1:
                players[winner] = 0
            
            if players[loser] == -1:
                players[loser] = 0
            
            # increment the losers count everytime
            players[loser] += 1
        
        for i, player in enumerate(players):
            # if player has played and hasnt lost any matches, add to winners
            if player == 0:
                answer[0].append(i)
                
            # if player has lost only 1 match, add to second array
            if player == 1:
                answer[1].append(i)
                
        return answer