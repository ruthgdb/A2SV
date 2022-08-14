class Solution:
    def frequencySort(self, s: str) -> str:
        sets = set(s)
        freq = [[s.count(i), i] for i in sets]
        freq.sort(reverse = True)
        res = []
        
        for el in freq:
            res.append(el[0] * el[1])
            
        return ''.join(res)