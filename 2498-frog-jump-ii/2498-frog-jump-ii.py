class Solution:
    def maxJump(self, stones: List[int]) -> int:
        if len(stones) == 2:
            return abs(stones[0] - stones[1])
        
        maxJump = 0
        
        for i in range(2, len(stones)):
            maxJump = max(maxJump, stones[i] - stones[i - 2])
            
        return maxJump