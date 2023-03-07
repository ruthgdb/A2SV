class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = min(time)
        right = left * totalTrips
        
        def completeTrips(trips):
            count = 0
            
            for t in time:
                count += trips // t
             
            return count >= totalTrips
        
        while left < right:
            mid = (left + right) // 2
            canComplete = completeTrips(mid)
            
            if canComplete:
                right = mid
            else:
                left = mid + 1
                
        return left