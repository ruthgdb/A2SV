class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = [[] for _ in range(numRows)]
        res = []
        i = 0
        upward = False
        
        for char in s:
            rows[i].append(char)
            if upward:
                i -= 1
                if i == -1:
                    upward = False
                    i = 1
            else:
                i += 1
                if i == len(rows):
                    upward = True
                    i -= 2
                    
        for row in rows:
            res.append("".join(row))
            
        return ''.join(res)