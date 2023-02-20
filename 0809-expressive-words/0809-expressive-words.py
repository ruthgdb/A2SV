class Solution:
    def groupWords(self, word):
        groups = []
        temp = []
        
        for i in word:
            if not temp or temp[-1] == i:
                temp.append(i)
            elif temp:
                groups.append(''.join(temp))
                temp = [i]
            
        if temp:
            groups.append(''.join(temp))
            
        return groups
    
    def expressiveWords(self, s: str, words: List[str]) -> int:
        s = self.groupWords(s) 
        count = 0
        
        for word in words:
            temp = self.groupWords(word)
            if len(s) != len(temp):
                continue
            
            isStrechy = True
            for i in range(len(s)):
                if len(temp[i]) == len(s[i]) and temp[i][0] == s[i][0]:
                    continue
                    
                if len(s[i]) < 3 or len(s[i]) < len(temp[i]) or temp[i][0] != s[i][0]:
                    isStrechy = False
                    
            if isStrechy:
                count += 1
                
        return count