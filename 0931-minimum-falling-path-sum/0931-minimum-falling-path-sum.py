class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        MinimumFallingPathSum = min(matrix[0])
        
        for i in range(1, len(matrix)):
            currMin = float("inf")
            
            for j in range(len(matrix[0])):
                left = matrix[i - 1][j - 1] if j - 1 >= 0 else float("inf")
                top = matrix[i - 1][j]
                right = matrix[i - 1][j + 1] if j + 1 < len(matrix[0]) else float("inf")
                
                matrix[i][j] += min(left, right, top)
                currMin = min(currMin, matrix[i][j])
            MinimumFallingPathSum = currMin
                
        return MinimumFallingPathSum