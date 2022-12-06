class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefixSum = []
        postfixSum = [0]
        
        # find the prefix sum of the array
        for num in nums:
            if not prefixSum:
                prefixSum.append(num)
            else:
                prefixSum.append(prefixSum[-1] + num)
            
        # find the postfix sum of the array
        for num in reversed(nums):
            postfixSum.append(postfixSum[-1] + num)
        
        postfixSum.reverse()
        
        for i in range(len(nums)):
            if prefixSum[i] == postfixSum[i]:
                return i
     
        return -1