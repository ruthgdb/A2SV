class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        length = len(palindrome)
        
        if length == 1:
            return ""
        
        result = ''
        
        for i in range(length // 2):
            if palindrome[i] != 'a':
                result = palindrome[:i] + 'a' + palindrome[i + 1:]
                break
                
        if result == '':
            result = palindrome[:length - 1] + 'b'
                
        return result