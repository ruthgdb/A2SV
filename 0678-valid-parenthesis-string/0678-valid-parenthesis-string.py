class Solution:
    def checkValidString(self, s: str) -> bool:
        opens = 0
        close = 0
        asterisk = 0
        
        for i in s:
            if i == '(':
                opens += 1
            if i == ')':
                close += 1
            if i == '*':
                asterisk += 1
                
            if close > asterisk + opens:
                return False
            
        opens = 0
        close = 0
        asterisk = 0
        
        for i in reversed(s):
            if i == '(':
                opens += 1
            if i == ')':
                close += 1
            if i == '*':
                asterisk += 1
                
            if opens > asterisk + close:
                return False
            
        return True