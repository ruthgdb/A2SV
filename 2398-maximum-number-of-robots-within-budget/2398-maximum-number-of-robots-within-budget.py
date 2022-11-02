class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        left = 0
        curr_sum = 0
        max_len = 0
        max_q = deque()
        
        for right in range(n):
            while max_q and chargeTimes[right] > max_q[-1]:
                max_q.pop()
                
            max_q.append(chargeTimes[right])
            curr_sum += runningCosts[right]
            
            while max_q and max_q[0] + ((right - left + 1) * curr_sum) > budget:
                if max_q[0] == chargeTimes[left]:
                    max_q.popleft()
                curr_sum -= runningCosts[left]
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len