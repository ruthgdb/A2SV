class Solution:
    def completeTrips(self, trips, times, totalTrips):
        count = 0

        for time in times:
            count += trips // time

        return count >= totalTrips

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = min(time)
        right = left * totalTrips

        while left < right:
            mid = (left + right) // 2

            if self.completeTrips(mid, time, totalTrips):
                right = mid
            else:
                left = mid + 1
                
        return left