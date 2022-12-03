class Solution:
    def frequencySort(self, s: str) -> str:
        res = []
        count = Counter(s)
        freq = [(count[i], i) for i in count]
        freq.sort(reverse = True)
        
        for c, letter in freq:
            res.append(letter * c)
        
        return ''.join(res)