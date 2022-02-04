class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''
        6, 5, 3, 1, 0
        
        i = 0
        i<5 and cit[0] > 0
           i++
           
        i = 0
        1
        2
        3
        
        '''
        if not citations:
            return 0
        
        citations = sorted(citations, reverse=True)
        hIndex = 0
        
        while hIndex < len(citations) and citations[hIndex] > hIndex:
            hIndex += 1
            
        return hIndex 