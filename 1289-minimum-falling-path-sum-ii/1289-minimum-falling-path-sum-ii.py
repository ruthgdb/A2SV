class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:    
        
        for i in range(1, len(matrix)):
            currRow = sorted([(matrix[i - 1][x], x) for x in range(len(matrix[0]))])
            
            for j in range(len(matrix[0])):
                currMin = matrix[i][j]
                if currRow[0][1] == j:
                    currMin += currRow[1][0]
                else:
                    currMin += currRow[0][0]
                    
                matrix[i][j] = currMin
          
        return min(matrix[-1])