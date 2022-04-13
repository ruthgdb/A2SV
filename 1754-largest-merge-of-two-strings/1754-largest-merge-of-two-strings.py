class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merged = []
        
        while word1 != '' and word2 != '':
            if word1 < word2:
                merged.append(word2[0])
                word2 = word2[1:]
            else:
                merged.append(word1[0])
                word1 = word1[1:]
                
        merged.append(word1)
        merged.append(word2)
                
        return ''.join(merged)