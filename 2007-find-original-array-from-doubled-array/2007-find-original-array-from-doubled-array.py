class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        
        changed.sort()
        org = []
        c = Counter(changed)
        
        for i in changed:
            if c[i] == 0:
                continue
            
            if (i == 0 and c[i] < 2) or (i > 0 and (c[i] < 1 or c[i*2] < 1)):
                return []
            
            org.append(i)
            c[i] -= 1
            c[i*2] -= 1 
        
        return org