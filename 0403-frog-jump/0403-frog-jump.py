class Solution:
    def canCross(self, stones: List[int]) -> bool:
        indices = defaultdict(int)
        
        for i, stone in enumerate(stones):
            indices[stone] = i
           
        @cache
        def dp(i, k):
            if i == len(stones) - 1:
                return True
            
            can_jump = False
            first = k - 1 + stones[i] if k >= 2 else float('inf')
            second = k + stones[i] if k >= 1 else float('inf')
            third = k + 1 + stones[i]
            
            if first != float('inf') and first in indices:
                can_jump = dp(indices[first], k - 1)
            
            if second != float('inf') and second in indices:
                can_jump |= dp(indices[second], k)
            
            if third in indices:
                can_jump |= dp(indices[third], k + 1)

            return can_jump
        
        return dp(0, 0)