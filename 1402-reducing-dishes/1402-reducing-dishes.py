class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)
        runningSum = 0
        prevSum = 0
        maxSum = 0
        
        for i in range(len(satisfaction)):
            prevSum = prevSum + runningSum + satisfaction[i]
            runningSum += satisfaction[i]
            maxSum = max(maxSum, prevSum)
                
        return maxSum