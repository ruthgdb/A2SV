class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        mapping = {
            '2':['a', 'b', 'c'],
            '3':['d', 'e', 'f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z']
        }
        
        def backtrack(i, path):
            if i == len(digits):
                if path:
                    res.append(''.join(path))
                return
            
            for j in mapping[digits[i]]:
                path.append(j)
                backtrack(i + 1, path)
                path.pop()
            
        backtrack(0, [])
        return res