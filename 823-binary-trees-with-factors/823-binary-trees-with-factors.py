class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = {num: 1 for num in arr}
        mod = 10 ** 9 + 7
        
        for i, el in enumerate(arr):
            for j in range(i):
                if el % arr[j] == 0 and el // arr[j] in dp:
                    dp[el] += dp[arr[j]] * dp[el // arr[j]]
                    
        return sum(dp.values()) % mod