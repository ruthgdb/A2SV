class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper + lower != sum(colsum):
            return []
        
        n = len(colsum)
        matrix = [[0 for x in range(n)],  [0 for x in range(n)]]

        for i in range(n):
            if colsum[i] == 2:
                matrix[0][i], matrix[1][i] = 1, 1
                upper, lower = upper - 1, lower - 1
                
        for i in range(n):
            if colsum[i] == 1:
                if upper > 0:
                    matrix[0][i] = 1 
                    upper -= 1
                else:
                    matrix[1][i] = 1 
                    lower -= 1
        
        return [] if upper != 0 or lower != 0 else matrix