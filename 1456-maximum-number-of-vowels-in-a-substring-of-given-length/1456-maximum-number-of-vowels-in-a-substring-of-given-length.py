class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        left = 0
        maxLen = 0
        
        for right in range(len(s)):
            if s[right] in vowels:
                count += 1
            
            if right - left + 1 > k:
                if s[left] in vowels:
                    count -= 1
                    
                left += 1
                
            maxLen = max(maxLen, count)
            
        return maxLen