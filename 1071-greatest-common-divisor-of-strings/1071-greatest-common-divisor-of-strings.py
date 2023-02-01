class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = []
        possibles = []
        
        def checkPrefix(word):
            for i in range(0, len(str1), len(word)):
                if str1[i:i + len(word)] != word:
                    return False
                
            for i in range(0, len(str2), len(word)):
                if str2[i:i + len(word)] != word:
                    return False
                
            return True
        
        for i in range(min(len(str1), len(str2))):
            if str1[i] != str2[i]:
                break
            
            ans.append(str1[i])
            possibles.append(''.join(ans))
            
        for curr in reversed(possibles):
            if checkPrefix(curr):
                return curr
            
        return ""