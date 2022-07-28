class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        freqS, freqT = Counter(s), Counter(t)
        return freqS == freqT