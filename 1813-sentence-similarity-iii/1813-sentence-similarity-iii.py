class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1, s2 = sentence1.split(' '), sentence2.split(' ')
        
        if len(s1) > len(s2):
            s1, s2 = s2, s1
            
        i, j = 0, len(s1) - 1
        m, n = 0, len(s2) - 1
        
        while i < len(s1):
            if s1[i] == s2[m]:
                i += 1
                m += 1 
            else:
                break
                
        while j >= 0:    
            if s1[j] == s2[n]:
                j -= 1
                n -= 1
            else:
                break    
                
        return i > j