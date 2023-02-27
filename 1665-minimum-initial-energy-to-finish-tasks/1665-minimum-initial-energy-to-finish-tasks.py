class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse = True)
        total = 0
        res = 0
        
        for actual, minimum in tasks:
            if total < minimum:
                res += minimum - total
                total = minimum - actual
            else:
                total -= actual
            
        return res