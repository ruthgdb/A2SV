import heapq

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        '''
        -10, 0, 2, 5, 8, 10, 12, 20
        
        min = [10, 0, -2, -5]
        max = [8, 10, 12, 20]
        
        len = 6
        windiw size = 6 - 3 = 3
        min_diff = 30
        if len <= 3: 0
        
        left = 0, right = 2, min_diff = 12
        left = 1, right = 3, min_diff = 10
        left = 2, right = 4, min_diff = 10
        left = 3, right = 5, min_diff = 10
        
        TC: O(n log n), n = len(nums)
        SC: O(1)
        
        '''
        
        def find_range(arr):
            min_values = []
            max_values = []
            
            for num in arr:
                heappush(min_values, -num)
                heappush(max_values, num)
                
                if len(min_values) > 4:
                    heappop(min_values)
                    
                if len(max_values) > 4:
                    heappop(max_values)
                    
            min_values = [-num for num in min_values]
        
            return min_values + max_values
        
        if len(nums) <= 3:
            return 0
        
        
        if len(nums) > 8:
            min_max_vals = find_range(nums)
        else:
            min_max_vals = nums.copy()
        
        min_max_vals.sort()
        window_size = len(min_max_vals) - 3
        left = 0
        min_diff = min_max_vals[-1] - min_max_vals[0]
        
        for right in range(len(min_max_vals)):
            if right - left + 1 > window_size:
                left += 1
                
            if right - left + 1 == window_size:
                min_diff = min(min_diff, min_max_vals[right] - min_max_vals[left])
                
        return min_diff