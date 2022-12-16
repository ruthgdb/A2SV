class Solution:
    def checkValidString(self, s: str) -> bool:
        
        @cache
        def dp(i, count):
            if i == len(s):
                return count == 0
            
            if count < 0:
                return False
            
            ifOpen = ifClose = ifEmpty = False
            
            if s[i] == '*':
                ifOpen = dp(i + 1, count + 1)
                ifClose = dp(i + 1, count - 1)
                ifEmpty = dp(i + 1, count)
            elif s[i] == '(':
                ifOpen = dp(i + 1, count + 1)
            else:
                ifClose = dp(i + 1, count - 1)
                
            return ifOpen or ifClose or ifEmpty
            
        return dp(0, 0)