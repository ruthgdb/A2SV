class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        concatinatedWords = []
        
        @cache
        def dp(i, word):
            if i == len(word):
                return True
            
            for j in range(i, len(word)):
                
                if word[i: j + 1] in wordSet:
                    if dp(j + 1, word):
                        return True
                    
            return False
            
        for word in words:
            wordSet.remove(word)
            if dp(0, word):
                concatinatedWords.append(word)
            wordSet.add(word)
            
        return concatinatedWords