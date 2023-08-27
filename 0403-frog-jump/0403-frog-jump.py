import bisect

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        @cache
        def dp(i, k):
            if i == len(stones) - 1:
                return True
            
            first = second = third = False
            first_nxt_jump = bisect_left(stones, k - 1 + stones[i], i, len(stones) - 1)
            second_nxt_jump = bisect_left(stones, k + stones[i], i + 1, len(stones) - 1)
            third_nxt_jump = bisect_left(stones, k + 1 + stones[i], i + 1, len(stones) - 1)
            
            if stones[first_nxt_jump] - (k - 1) == stones[i]:
                first = dp(first_nxt_jump, k - 1)
            
            if stones[second_nxt_jump] - k == stones[i]:
                second = dp(second_nxt_jump, k)
            
            if stones[third_nxt_jump] - (k + 1) == stones[i]:
                third = dp(third_nxt_jump, k + 1)

            return first or second or third
        
        return dp(0, 0)