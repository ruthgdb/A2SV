class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        starts = [event[0] for event in events]
        
        @cache
        def dp(i, count):
            if i == len(events) or count == k:
                return 0
            
            cont = 0
            
            if count < k:
                idx = bisect.bisect_right(starts, events[i][1])
                cont = events[i][2] + dp(idx, count + 1)
                
            start = dp(i + 1, count)
            return max(start, cont)
        
        return dp(0, 0)
        