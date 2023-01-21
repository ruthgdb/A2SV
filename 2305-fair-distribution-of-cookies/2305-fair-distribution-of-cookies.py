class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0] * k
        minDiff = float("inf")
        
        @cache
        def backtrack(i, currMax):
            nonlocal minDiff
            
            if i == len(cookies):
                minDiff = min(minDiff, max(children))
                return 
            
            for j in range(k):
                children[j] += cookies[i]
                if children[j] < minDiff:
                    backtrack(i + 1, max(currMax, children[j]))
                children[j] -= cookies[i]
                
            return currMax
        
        backtrack(0, 0)
        return minDiff