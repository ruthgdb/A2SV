class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        org = []
        s = len(changed)
        c = Counter(changed)
        if s % 2 == 0:
            for i in changed:
                if c[i] > 0 and c[2*i] > 0:              
                    if i != 0:
                        org.append(i)
                        c[i] -= 1
                        c[2*i] -= 1                    
                    elif c[i] > 1:
                        org.append(i)
                        c[i] -= 1
                        c[2*i] -= 1
                        
                                        
        if len(changed) // 2 == len(org):
            return org
        return []