class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, maxx = 0, 0, 0
        count = defaultdict(int)
        
        while right < len(s):
            count[s[right]] += 1
            
            if (right - left + 1) - max(count.values()) > k:
                # print(right, left, count)
                count[s[left]] -= 1
                left += 1
                
            maxx = max(maxx, right - left + 1)
                
                # print(count, left,right)
            right += 1
            # print(count, left, right)
            
        return maxx