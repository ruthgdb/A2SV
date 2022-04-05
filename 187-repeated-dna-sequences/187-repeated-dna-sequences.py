class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequence = dict()
        res = set()
        
        for i in range(len(s)):
            temp = s[i:i+10]
            
            if temp in sequence.keys():
                res.add(temp)
            else:
                sequence[temp] = 0
                
        return list(res)