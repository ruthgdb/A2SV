class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = len(strs[0])
        
        for i in range(1, len(strs)):
            count = 0
            mini = min(len(strs[0]), len(strs[i]))
            for j in range(mini):
                if strs[i][j] == strs[0][j]:
                    count += 1
                else:
                    break
            l = min(l, count)
                    
        return strs[0][:l]