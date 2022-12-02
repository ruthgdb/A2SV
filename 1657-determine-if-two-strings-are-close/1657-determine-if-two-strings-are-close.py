class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        countWord1 = Counter(word1)
        countWord2 = Counter(word2)
        
        return countWord1.keys() == countWord2.keys() and sorted(countWord1.values()) == sorted(countWord2.values()) 