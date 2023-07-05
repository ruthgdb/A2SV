class Solution:
    def longestWord(self, words: List[str]) -> str:
        valid_words = set([""])
        res = ''
        words.sort(key = lambda x: (-len(x), x))
        words.reverse()
        
        for word in words:
            if word[:-1] in valid_words:
                res = word
                valid_words.add(word)
            
        return res