class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        mapping = {}
        
        for i in range(65, 91):
            mapping[chr(i)] = i - 64
            
        res = mapping[columnTitle[0]]
            
        for i in range(1, len(columnTitle)):
            res = res * 26 + mapping[columnTitle[i]]
        
        return res