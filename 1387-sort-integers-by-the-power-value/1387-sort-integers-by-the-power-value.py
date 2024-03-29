import heapq
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        res = []
        
        @cache
        def dp(i):
            if i == 1:
                return 0
            
            if i % 2 == 0:
                return dp(i // 2) + 1
            
            return dp(3 * i + 1) + 1
        
        for i in range(lo, hi + 1):
            power = dp(i)
            heappush(res, (-power, -i))
            
            if len(res) > k:
                heappop(res)
         
        return -res[0][1]