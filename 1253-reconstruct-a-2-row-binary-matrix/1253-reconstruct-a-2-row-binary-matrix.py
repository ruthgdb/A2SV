class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper + lower != sum(colsum):
            return []
        
        matrix, n, u, l = [], len(colsum), upper, lower
        
        for _ in range(2):
            temp = [0 for x in range(n)]
            matrix.append(temp)
            
        for i in range(n):
            if colsum[i] == 2:
                matrix[0][i], matrix[1][i] = 1, 1
                u -= 1
                l -= 1
                
        for i in range(n):
            if colsum[i] == 1:
                if u > 0:
                    matrix[0][i] = 1 
                    u -= 1
                else:
                    matrix[1][i] = 1 
                    l -= 1
        
        return [] if sum(matrix[0]) != upper or sum(matrix[1]) != lower else matrix