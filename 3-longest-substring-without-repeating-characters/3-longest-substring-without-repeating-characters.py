class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        words = set()
        count, maxx = 0, 0
        
        for i in range(len(s)):
            words = set()
            count = 0
            j = i
            while j < len(s) and s[j] not in words:
                words.add(s[j])
                count += 1
                j += 1
            maxx = max(maxx, count)
            
        return maxx