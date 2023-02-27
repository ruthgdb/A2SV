class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs.sort()
        maxPop = 1
        maxCount = float("-inf")
        
        for birth1, death1 in logs:
            count = 0
            
            for birth2, death2 in logs:
                if birth2 <= birth1 < death2:
                    count += 1
            
            if count > maxCount:
                maxCount = count
                maxPop = birth1
                
        return maxPop