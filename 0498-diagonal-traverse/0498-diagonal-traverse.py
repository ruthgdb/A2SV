class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        '''
           0 1 2
           
       0  [1,2,3]
       1  [4,5,6] 
       2  [7,8,9]
       
       neg = (0, 0), (1, 1), (2, 2)    (1, 0), (2, 1)     (2, 0)
       pos = (0, 2), (1, 1), (2, 0)   (0, 1), (1, 0)    (0, 0)  
       
       0: 1
       1: 2, 4
       2: 3, 5, 7
       3: 6, 8
       4: 9
         
        '''
        n = len(mat)
        m = len(mat[0])
        diagonals = defaultdict(list)
        answer = []
        
        for i in range(n):
            for j in range(m):
                diagonals[i + j].append(mat[i][j])
                
        for i in range(len(diagonals) + 1):
            if i % 2 == 0:
                answer.extend(diagonals[i][::-1])
            else:
                answer.extend(diagonals[i])
                
        return answer
            