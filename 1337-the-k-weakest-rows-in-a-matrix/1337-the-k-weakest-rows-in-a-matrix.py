class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        n = len(mat)
        m = len(mat[0])
        count = 0
        
        for i in range(n):
            count = 0
            for j in range(m):
                if mat[i][j] == 1:
                    count += 1
            res.append((count, i))
            
        res.sort()
        res = res[:k]
        
        res = [x[1] for x in res]
            
        return res
                