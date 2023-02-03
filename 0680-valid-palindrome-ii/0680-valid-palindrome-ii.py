class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        def check(st):
            return st == st[::-1]
        
        while left < right:
            if s[left] != s[right]:
                return check(s[:left] + s[left + 1:]) or check(s[:right] + s[right + 1:])   
            else:
                left += 1
                right -= 1
                
        return True
            