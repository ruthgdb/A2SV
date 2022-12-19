class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        opens = 0
        close = 0
        wildCards = 0
        
        for i in range(len(s)):
            if locked[i] == '0':
                wildCards += 1
            elif s[i] == '(':
                opens += 1
            elif s[i] == ')':
                close += 1
                
            if close > wildCards + opens:
                return False
           
        opens = 0
        close = 0
        wildCards = 0
        
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0':
                wildCards += 1
            elif s[i] == '(':
                opens += 1
            elif s[i] == ')':
                close += 1
                
            if opens > wildCards + close:
                return False
            
        return True