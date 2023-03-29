class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        maxSum = 0
        
        for i in range(len(satisfaction)):
            runningSum = 0
            idx = 1
            
            for j in range(i, len(satisfaction)):
                runningSum += satisfaction[j] * idx
                idx += 1
            
            maxSum = max(maxSum, runningSum)
                
        return maxSum