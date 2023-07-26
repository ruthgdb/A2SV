class Solution:
    def is_valid_speed(self, speed, arr, hour):
        time = 0
        
        for i, dist in enumerate(arr):
            curr_speed = dist/speed
            
            if i == len(arr) - 1:
                time += curr_speed
            else:
                time += math.ceil(curr_speed)
            # print(curr_speed, speed)
          
        # print('final', time <= hour)
        return time <= hour
        
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left = 1
        right = 10 ** 9
        best = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            is_valid = self.is_valid_speed(mid, dist, hour)
            
            if is_valid:
                best = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return best