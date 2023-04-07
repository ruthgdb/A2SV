class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        dp = {0}
        min_diff = float("inf")
        above_target = float("inf")
        
        for i in range(len(mat)):
            temp = set()
            above_temp = float("inf")
            
            for j in range(len(mat[0])):
                for k in dp:
                    if mat[i][j] + k <= target:
                        temp.add(mat[i][j] + k)
                    else:
                        above_temp = min(above_temp, mat[i][j] + k)
                        
                above_temp = min(above_temp, mat[i][j] + above_target)
                        
            dp = temp
            above_target = above_temp
          
        for total in dp:
            min_diff = min(min_diff, target - total)
        
        return min(min_diff, above_target - target)