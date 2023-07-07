class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        freq_count = Counter(s)
        unique_count = len(freq_count)
        max_len = 0
        
        for l in range(1, unique_count + 1):
            left = 0
            chars = defaultdict(int)
            
            for right in range(len(s)):
                chars[s[right]] += 1
                
                while len(chars) > l:
                    chars[s[left]] -= 1
                    if chars[s[left]] == 0:
                        del chars[s[left]]
                    left += 1
                
                if min(chars.values()) >= k:
                    max_len = max(max_len, right - left + 1)
                
        return max_len