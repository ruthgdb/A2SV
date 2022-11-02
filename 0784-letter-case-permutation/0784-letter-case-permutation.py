class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        
        def backtrack(idx, path):
            # if we've reach the end of our string, add the path to the result
            if idx == len(s):
                result.append(''.join(path))
                return
            
            # if its a number, just add it and continue
            if s[idx].isdigit():
                path.append(s[idx])
                backtrack(idx + 1, path)
                path.pop()
            else:
                # if its an alphabet
                # add it as lower case and continue
                
                path.append(s[idx].lower())
                backtrack(idx + 1, path)
                path.pop()
                
                # then also add it as upper case and continue
                path.append(s[idx].upper())
                backtrack(idx + 1, path)
                path.pop()
                
            
        backtrack(0, [])
        return result