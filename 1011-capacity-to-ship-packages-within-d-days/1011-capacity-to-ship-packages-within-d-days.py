class Solution:
    def count_days(self, cap, weights):
        max_weight = 1
        size = 0
        
        for weight in weights:
            if size + weight <= cap:
                size += weight
            else:
                max_weight += 1
                size = weight  
        
        return max_weight
        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            
            count = self.count_days(mid, weights)
            if count > days:
                left = mid + 1
            else:
                right = mid
        
        return left