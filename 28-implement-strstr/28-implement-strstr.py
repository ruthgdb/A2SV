class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        
        for i in range(len(haystack)):
            temp = haystack[i:i + n]
            if temp == needle:
                return i
            
        return -1