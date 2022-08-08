class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        
        def makeZero(i, j):
            for idx in range(m):
                if matrix[i][idx] != 0:
                    matrix[i][idx] = "0"
            
            for idx in range(n):
                if matrix[idx][j] != 0:
                    matrix[idx][j] = "0"
            
            
        for i in range(n):
            for j in range(m):
                if not matrix[i][j]:
                    makeZero(i, j)
                    