class Solution:
    def is_running(self, minutes, batteries, n, remaining):
        count = 0
        
        for i in range(n):
            if batteries[i] < minutes:
                count += minutes - batteries[i]
        
        return remaining >= count
        
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left = 1
        right = math.ceil(sum(batteries) / n)
        max_time = 1
        batteries.sort(reverse = True)
        remaining = sum(batteries[n:])
        
        while left <= right:
            mid = (left + right) // 2
            
            if self.is_running(mid, batteries, n, remaining):
                max_time = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return max_time