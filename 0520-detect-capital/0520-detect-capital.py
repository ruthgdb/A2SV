class Solution:
    def isAllCap(self, word):
        for char in word:
            if char.islower():
                return False
            
        return True
    
    def isAllLower(self, word):
        for char in word:
            if char.isupper():
                return False
            
        return True
    
    def isFirstCap(self, word):
        if word[0].islower():
            return False
        
        for i in range(1, len(word)):
            if word[i].isupper():
                return False
            
        return True
    
    def detectCapitalUse(self, word: str) -> bool:
        return self.isAllCap(word) or self.isAllLower(word) or self.isFirstCap(word)