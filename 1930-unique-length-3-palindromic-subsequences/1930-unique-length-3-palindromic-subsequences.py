class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        prefSum = [[0] * 26]
        postSum = [[0] * 26]
        res = set()
        
        for i in s:
            temp = prefSum[-1][:]
            temp[ord(i) - ord('a')] += 1
            prefSum.append(temp)
            
        for i in range(len(s) - 1, -1, -1):
            temp = postSum[-1][:]
            temp[ord(s[i]) - ord('a')] += 1
            postSum.append(temp)
            
        prefSum = prefSum[1:]
        postSum.pop()
        postSum.reverse()
        
        for i in range(1, len(s) - 1):
            for j in range(26):
                if prefSum[i - 1][j] > 0 and postSum[i][j] > 0:
                    res.add(chr(j + 97) + s[i] + chr(j + 97))
                    
        return len(res)