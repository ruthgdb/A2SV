class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        
        def backtrack(i, path):
            res.add(tuple(sorted(path)))

            for j in range(i , len(nums)):
                path.append(nums[j])
                backtrack(j + 1, path)
                path.pop()
            
        backtrack(0, [])
        return sorted(res)