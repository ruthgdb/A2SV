class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        subsets = [0] * k
        nums.sort(reverse = True)
        total = sum(nums)
        target = total // k
        memo = {}
        
        if total % k != 0:
            return False
        
        def backtrack(i):
            if i == len(nums):
                return True
            
            temp = tuple(subsets)
            if temp in memo:
                return memo[temp]
                        
            for j in range(k):
                if subsets[j] + nums[i] <= target:
                    subsets[j] += nums[i]
                    if backtrack(i + 1):
                        return True
                    subsets[j] -= nums[i]
                    
            memo[temp] = False
            
            return False
                        
        return backtrack(0)