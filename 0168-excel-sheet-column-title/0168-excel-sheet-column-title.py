class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        
        while columnNumber > 26:
            count = columnNumber % 26
            if count == 0:
                count = 26
            
            columnNumber -= count
            columnNumber //= 26
            res.append(chr(65 + count - 1))
           
        if columnNumber > 0:
            res.append(chr(65 + columnNumber - 1))
            
        res.reverse()
        return "".join(res)