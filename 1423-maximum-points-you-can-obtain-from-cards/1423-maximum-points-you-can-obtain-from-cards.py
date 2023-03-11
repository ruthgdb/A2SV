class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        k = len(cardPoints) - k
        left = 0
        total = sum(cardPoints)
        runningSum = 0
        maxPoints = 0
        
        for right in range(len(cardPoints)):
            runningSum += cardPoints[right]
            
            if right - left + 1 > k:
                runningSum -= cardPoints[left]
                left += 1
            
            if right - left + 1 == k:
                maxPoints = max(maxPoints, total - runningSum)
                
        return maxPoints