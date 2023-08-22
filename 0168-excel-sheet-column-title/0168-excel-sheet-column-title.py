class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        
        while columnNumber > 0:
            columnNumber -= 1
            count = columnNumber % 26
            columnNumber //= 26
            res.append(chr(65 + count))
 
        res.reverse()
        return "".join(res)