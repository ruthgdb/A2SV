class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        matches = dict()
        isMatching = True
        
        for word in words:
            matches, isMatching = {}, True
            for i in range(len(word)):
                if word[i] not in matches:
                    if pattern[i] not in matches.values():
                        matches[word[i]] = pattern[i]
                    else:
                        isMatching = False
                else:
                    if matches[word[i]] != pattern[i]:
                        isMatching = False
            if isMatching:
                res.append(word)
            
        return res