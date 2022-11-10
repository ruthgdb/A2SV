class Solution:
    def simplifyPath(self, path: str) -> str:
        canonical_path = []
        path = path.split('/')

        for char in path:
            if char == '' or char == '.':
                continue
            if char == '..':
                if canonical_path:
                    canonical_path.pop()
                continue
    
            canonical_path.append(char)
            
        return '/' + '/'.join(canonical_path)