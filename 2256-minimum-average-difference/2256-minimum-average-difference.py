class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefixSum = [0]
        postfixSum = [0]
        minAvgDiff = float("inf")
        minIdx = 0
        
        # find the prefix sum of the array
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)
            
        # find the postfix sum of the array
        for num in reversed(nums):
            postfixSum.append(postfixSum[-1] + num)
        
        postfixSum.reverse()
        
        # find the average difference at each index
        for i in range(1, len(prefixSum)):
            left = prefixSum[i] // i
            right = postfixSum[i] // (len(nums) - i) if i != len(nums) else 0
            currAvgDiff = abs(right - left)
            
            if currAvgDiff < minAvgDiff:
                minIdx = i - 1
                minAvgDiff = currAvgDiff
                
        return minIdx