class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        longest_beautiful_sentence = 0
        curr_len = int(word[0] == 'a')
        valid_char = {
            'a': {'a'}, 
            'e': {'a', 'e'}, 
            'i': {'e', 'i'}, 
            'o': {'i', 'o'}, 
            'u': {'o', 'u'}}
        
        is_beautiful = [word[0] == 'a', False, False, False, False]
        idx = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        
        for i in range(1, len(word)):
            if word[i - 1] in valid_char[word[i]]:
                curr_len += 1
                is_beautiful[idx[word[i]]] = True
            elif word[i] == 'a':
                curr_len = 1
                is_beautiful = [True, False, False, False, False]
            else:
                curr_len = 0
                is_beautiful = [False, False, False, False, False]
                
            if all(is_beautiful) == True:
                longest_beautiful_sentence = max(longest_beautiful_sentence, curr_len)
            
        return longest_beautiful_sentence