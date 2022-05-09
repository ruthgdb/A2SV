class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        match = dict()
        
        for i in range(len(s)):
            if s[i] in match and match[s[i]] != t[i]:
                return False
            if s[i] not in match and t[i] in match.values():
                return False
            elif s[i] not in match and t[i]:
                match[s[i]] = t[i]
                
        return True