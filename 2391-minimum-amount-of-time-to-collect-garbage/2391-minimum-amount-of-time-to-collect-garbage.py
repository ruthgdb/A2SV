class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        paper = 0
        pt = 0
        
        for i in range(len(garbage)):
            count = garbage[i].count('P')
            
            if i > 0:
                pt += travel[i - 1]
            
            if count > 0:
                paper += count + pt
                pt = 0
            
        glass = 0
        gt = 0
        
        for i in range(len(garbage)):
            count = garbage[i].count('G')
            
            if i > 0:
                gt += travel[i - 1]
            
            if count > 0:
                glass += count + gt
                gt = 0
      
        metal = 0
        mt = 0
        
        for i in range(len(garbage)):
            count = garbage[i].count('M')
            
            if i > 0:
                mt += travel[i - 1]
            
            if count > 0:
                metal += count + mt
                mt = 0
        
        return paper + metal + glass