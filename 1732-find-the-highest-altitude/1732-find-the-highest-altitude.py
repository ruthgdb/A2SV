class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currSum = 0
        maxSum = 0
        
        for alt in gain:
            currSum += alt
            maxSum = max(maxSum, currSum)
            
        return maxSum