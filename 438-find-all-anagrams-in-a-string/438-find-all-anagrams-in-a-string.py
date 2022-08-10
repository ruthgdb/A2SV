class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return
        
        countS, countP, left, right, res = defaultdict(int), Counter(p), 0, 0, []
        
        while right < len(s):
            countS[s[right]] += 1

            if right - left + 1 >= len(p):
                if countS == countP:
                    res.append(left)
                    
                if countS[s[left]] > 1:
                    countS[s[left]] -= 1
                else:
                    del countS[s[left]]
                
                left += 1 
            right += 1

        return res