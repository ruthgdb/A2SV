class Solution:
    def largestVariance(self, s: str) -> int:
        
        pairs = []
        unique_chars = set(s)
        
        for char in unique_chars:
            for char2 in unique_chars:
                if char == char2:
                    continue
                    
                pairs.append((char, char2))
        
        def check(s):
            max_variance = 0
            
            for pair in pairs:
                count1 = count2 = 0
                
                for l in s:
                    if l not in pair:
                        continue
                    elif l == pair[0] or l == pair[1]:
                        count1 += l == pair[0]
                        count2 += l == pair[1]
                        
                    if count1 < count2:
                        count1 = count2 = 0
                    elif count1 > 0 and count2 > 0:
                        max_variance = max(max_variance, count1 - count2)
            
            return max_variance
            
        return max(check(s), check(s[::-1]))