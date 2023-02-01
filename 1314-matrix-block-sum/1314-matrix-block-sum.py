class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        prefSum = []
        ans = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        
        def findSum(row, col):
            c1 = max(0, col - k)
            c2 = min(col + k + 1, len(prefSum[0]) - 1)
            r1 = max(0, row - k)
            r2 = min(row + k, len(prefSum) - 1)
            totalSum = 0
            
            for r in range(r1, r2 + 1):
                totalSum += prefSum[r][c2] - prefSum[r][c1]
                
            return totalSum
        
        for i in range(len(mat)):
            temp = [0]
            
            for j in range(len(mat[0])):
                temp.append(temp[-1] + mat[i][j])
                
            prefSum.append(temp)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                ans[i][j] = findSum(i, j)
                
        return ans