class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = Counter(s)
        l, odds, isOdd = 0, 0, False
            
        for letter in letters:
            if letters[letter] % 2 == 0:
                l += letters[letter]
            else:
                isOdd = True
                odds += letters[letter] - 1

        if isOdd:
            l += odds + 1
                    
        return l