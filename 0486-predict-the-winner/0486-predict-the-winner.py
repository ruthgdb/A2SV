class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def dfs(i, j):
            if i == j:
                return nums[i]
            
            return max(nums[i] - dfs(i + 1, j), nums[j] - dfs(i, j - 1))
        
        return dfs(0, len(nums) - 1) >= 0