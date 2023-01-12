class Solution:
    def isFirst(self, idx, count):
        for i in range(idx):
            if count[i] > 0:
                return False
            
        return True
    
    def robotWithString(self, s: str) -> str:
        t = []
        paper = []
        count = [0] * 26
        
        for i in s:
            count[ord(i) - ord('a')] += 1
        
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] -= 1
            t.append(s[i])
            
            while t:
                curr = t[-1]
                if self.isFirst(ord(curr) - ord('a'), count):
                    paper.append(t.pop())
                else:
                    break
            
        return "".join(paper)
        