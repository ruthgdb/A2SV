class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = l = 0
        lookup = {}
        
        for r in range(len(fruits)):
            lookup[fruits[r]] = 1 + lookup.get(fruits[r],0)
            
            while len(lookup) > 2:
                lookup[fruits[l]] -= 1
                
                if lookup[fruits[l]] == 0:
                    del lookup[fruits[l]]
                l += 1
                
            res = max(res,sum(lookup.values()))
        return res