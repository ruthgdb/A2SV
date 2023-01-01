class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        follows = defaultdict(str)
        
        if len(words) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            if words[i] in follows and pattern[i] != follows[words[i]]:
                return False
            
            follows[words[i]] = pattern[i]
            
        follows.clear()
        
        for i in range(len(pattern)):
            if pattern[i] in follows and words[i] != follows[pattern[i]]:
                return False
            
            follows[pattern[i]] = words[i]
            
        return True