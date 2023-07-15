class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        starts = [event[0] for event in events]
        
        @cache
        def dp(i, count):
            if i == len(events) or count == k:
                return 0
            
            idx = bisect.bisect_right(starts, events[i][1])
            take = events[i][2] + dp(idx, count + 1)
            skip = dp(i + 1, count)
            return max(take, skip)
        
        return dp(0, 0)
        