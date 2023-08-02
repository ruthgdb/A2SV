class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(i, path, seen):
            if i == len(nums):
                if len(path) == len(nums):
                    res.append(path.copy())
                    
            for j in range(len(nums)):
                if j not in seen:
                    seen.add(j)
                    path.append(nums[j])
                    dfs(i + 1, path, seen)
                    seen.remove(j)
                    path.pop()
            
        dfs(0, [], set())
        return res