class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1]
        
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
                
        return dp[0]
        
        
        
#         memo = dict()
        
#         def dfs(i, j):
#             if i == len(triangle):
#                 return 0
#             if (i, j) in memo.keys():
#                 return memo[(i, j)]
            
#             memo[(i, j)] = triangle[i][j] + min(dfs(i + 1, j), dfs(i + 1, j + 1)) 
#             return memo[(i, j)]
            
#         return triangle[0][0] + min(dfs(1, 0), dfs(1, 1))