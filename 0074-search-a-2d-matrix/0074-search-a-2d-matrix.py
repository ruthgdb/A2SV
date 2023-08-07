class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        row = -1
        
        # searching row
        while left <= right:
            mid = (left + right) // 2
            
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
                
            if matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        if row == -1:
            return False
       
        # searching col
        left = 0
        right = len(matrix[0]) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if target == matrix[row][mid]:
                return True
            
            if target < matrix[row][mid]:
                right = mid - 1
            else:
                left = mid + 1
                
        return False