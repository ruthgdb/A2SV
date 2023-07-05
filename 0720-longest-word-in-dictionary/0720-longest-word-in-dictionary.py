class Solution:
    def longestWord(self, words: List[str]) -> str:
        valid_words = set([""])
        res = ''
        words.sort(key = len)
        
        for word in words:
            if word[:-1] in valid_words:
                if (len(word) == len(res) and word < res) or len(word) > len(res):
                    res = word
                valid_words.add(word)
            
        return res