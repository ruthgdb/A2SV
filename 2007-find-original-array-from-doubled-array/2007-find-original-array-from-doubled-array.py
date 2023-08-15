class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        s = len(changed)
        if s % 2 != 0:
            return []
        
        changed.sort()
        org = []
        s = len(changed)
        c = Counter(changed)
        
        for i in changed:
            if c[i] > 0 and c[2*i] > 0:              
                if i != 0 or c[i] > 1:
                    org.append(i)
                    c[i] -= 1
                    c[2*i] -= 1 
        
        return org if len(changed) // 2 == len(org) else []