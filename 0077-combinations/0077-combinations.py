class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(i, path):
            if len(path) == k:
                res.append(path[:])
                return
            
            for j in range(i + 1, n + 1):
                path.append(j)
                backtrack(j, path)
                path.pop()
            
        for i in range(1, n + 1):
            backtrack(i, [i])
            
        return res