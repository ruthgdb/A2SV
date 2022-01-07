class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        for i in range(len(s)):
            if not s[i] in dic:
                if not t[i] in dic.values():
                    dic[s[i]] = t[i]
                else:
                    return False
            elif dic[s[i]] != t[i]:
                return False
        return True