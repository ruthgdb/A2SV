class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        numsCosts = [(nums[i], cost[i]) for i in range(len(nums))]
        numsCosts.sort()
        prefSumCosts = [numsCosts[0][1]]
        postSumCosts = 0
        
        for i in range(1, len(nums)):
            prefSumCosts.append(numsCosts[i][1] + prefSumCosts[-1])
            
        for i in range(1, len(nums)): 
            postSumCosts += numsCosts[i][1] * (numsCosts[i][0] - numsCosts[0][0])
            
        res = postSumCosts
        
        for i in range(1, len(nums)):
            curr = numsCosts[i][0] - numsCosts[i - 1][0]
            postSumCosts += prefSumCosts[i - 1] * curr
            postSumCosts -= curr * (prefSumCosts[len(nums) - 1] - prefSumCosts[i - 1])
            res = min(res, postSumCosts)
            
        return res