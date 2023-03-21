class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10 ** 9 + 7
        res = 0
        jumps = { 
                 0: [4, 6], 
                 1:[6,8],
                 2:[7,9],
                 3:[4,8],
                 4:[0,3,9],
                 5:[],
                 6:[0,1,7],
                 7:[6,2],
                 8:[1,3],
                 9:[2,4]
                }
        
        dp = [1] * 10
        
        for i in range(n - 1):
            temp = [0] * 10
            
            for j in range(10):
                for nxtJump in jumps[j]:
                    temp[j] += dp[nxtJump]
                    temp[j] = temp[j] % mod
                    
            dp = temp
        
        return sum(dp) % mod