class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        sequences = set()
        letters = Counter(tiles)
        
        def backtrack(path):
            if path:
                sequences.add(''.join(path))
            
            if sum(letters.values()) == 0:
                return
            
            for letter in letters:
                if letters[letter] > 0:
                    letters[letter] -= 1
                    backtrack(path + letter)
                    letters[letter] += 1
        
        backtrack('')
        return len(sequences)