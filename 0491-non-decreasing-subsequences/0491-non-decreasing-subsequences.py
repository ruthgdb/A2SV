class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        def backtrack(i, path):
            if len(path) > 1:
                ans.add(tuple(path))
                
            if i == len(nums):
                return
            
            for j in range(i, len(nums)):
                if not path:
                    backtrack(j + 1, [nums[j]])
                else:
                    if path[-1] <= nums[j]:
                        backtrack(j + 1, path + [nums[j]])
            
        backtrack(0, [])
        return ans