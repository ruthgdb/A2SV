class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maxLength = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    left = int(matrix[i][j - 1]) if j > 0 else 0
                    top = int(matrix[i - 1][j]) if i > 0 else 0
                    leftTop = int(matrix[i - 1][j - 1]) if j > 0 and i > 0 else 0
                    matrix[i][j] = min(left, top, leftTop) + 1
                    maxLength = max(maxLength, matrix[i][j])
                    
        return maxLength ** 2