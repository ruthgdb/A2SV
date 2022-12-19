class Solution:
    def isValid(self, s, isReversed):
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
            
            if isReversed:
                if opens > asterisk + close:
                    return False
            else:
                if close > asterisk + opens:
                    return False

        return True
    
    def checkValidString(self, s: str) -> bool:
        return self.isValid(s, False) and self.isValid(reversed(s), True)