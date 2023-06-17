class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        
        def dfs(arr):
            if len(arr) <= 2:
                return 1

            left = []
            right = []

            for i in range(1, len(arr)):
                if arr[i] < arr[0]:
                    left.append(arr[i])
                else:
                    right.append(arr[i]) 

            return dfs(left) * dfs(right) * math.comb(len(arr) - 1, len(left)) 

        return (dfs(nums) - 1) % mod