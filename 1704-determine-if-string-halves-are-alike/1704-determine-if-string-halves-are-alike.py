class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        vowelCount = 0
        consonantCount = 0
        half = len(s) // 2
        
        for i in range(len(s)):
            if s[i] in vowels:
                if i < half:
                    vowelCount += 1
                else:
                    vowelCount -= 1
            else:
                if i < half:
                    consonantCount += 1
                else:
                    consonantCount -= 1
                    
        return vowelCount == consonantCount == 0