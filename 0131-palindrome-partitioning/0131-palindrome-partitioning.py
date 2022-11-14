class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        
        def backtrack(idx, path):
            if idx == len(s):
                result.append(path[:])
                return
            
            for j in range(idx, len(s)):
                substring = s[idx:j + 1]
                if substring == substring[::-1]:
                    backtrack(j + 1, path + [substring])
            
        backtrack(0, [])
        return result