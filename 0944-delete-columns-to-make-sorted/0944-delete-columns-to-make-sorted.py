class Solution:
    def isSorted(self, s):        
        alph = [0] * 26
        
        for i in s:
            idx = ord(i) - ord('a')
            
            if sum(alph[idx + 1:]) != 0:
                return False
            
            alph[idx] += 1
            
        return True
    
    def minDeletionSize(self, strs: List[str]) -> int:
        delCols = 0
        
        for i in range(len(strs[0])):
            s = []
            
            for j in range(len(strs)):
                s.append(strs[j][i])
                
            if not self.isSorted(s):
                delCols += 1
                
        return delCols