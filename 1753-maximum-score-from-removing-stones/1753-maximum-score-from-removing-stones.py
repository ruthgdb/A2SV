class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        piles = [a, b, c]
        count = 0
    
        piles.sort()
        
        while piles[0] + piles[1] > piles[2]:
            piles[0] -= 1
            piles[1] -= 1
            count += 1
            
        count += piles[0] + piles[1]
        return count
       