class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indices = []
        count1 = Counter(p)
        count2 = defaultdict(int)
        left = 0
        
        for right in range(len(s)):
            count2[s[right]] += 1
            
            if right - left + 1 > len(p):
                count2[s[left]] -= 1
                if count2[s[left]] == 0:
                    del count2[s[left]]
                left += 1
                
            if count1 == count2:
                indices.append(left)
        
        return indices